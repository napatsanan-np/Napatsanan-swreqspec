# test ของ T-03: จองคิวสำเร็จ
# AC-BKG-01 (FR-BKG-04)
from tests.conftest import AUTH


def test_AC_BKG_01(client, make_slot):
    """AC-BKG-01: ยืนยันตัวตนแล้ว และช่วง 09.00 น. มีที่นั่งว่าง จองแล้วต้องสำเร็จ"""
    slot = make_slot(start="09:00", remaining=1)

    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    assert res.status_code == 201


def test_TC_BKG_01_1_book_last_seat(client, db, make_slot):
    """TC-BKG-01-1 (AC-BKG-01, FR-BKG-04): จองที่นั่งสุดท้ายของช่วง 09.00 น."""
    from sqlalchemy import select

    from app.db.models import Booking

    # Given ยืนยันตัวตนแล้ว (HN 0001234) และช่วง 09.00 น. มีที่นั่งว่าง 1 ที่
    slot = make_slot(start="09:00", remaining=1)

    # When POST /bookings ด้วย slot_id ของช่วง 09.00 น.
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then (1) บันทึกสำเร็จ: ได้ booking id กลับ และมีรายการจองของ HN นี้ที่ช่วงนั้นในฐานข้อมูล 1 รายการ
    body = res.json()
    assert body.get("booking_id") is not None
    bookings = db.scalars(
        select(Booking).where(Booking.hn == "0001234", Booking.slot_id == slot.id)
    ).all()
    assert len(bookings) == 1

    # Then (2) response มี queue_no ตาม plan ข้อ 4
    assert "queue_no" in body
    # ยังไม่ตรวจค่าและรูปแบบของหมายเลขคิว เพราะรอ Q-02

    # Then (3) remaining ของช่วง 09.00 น. เป็น 0
    db.refresh(slot)
    assert slot.remaining == 0


def test_TC_BKG_01_3_no_seat_left(client, db, make_slot):
    """TC-BKG-01-3 (AC-BKG-01 ขอบ, FR-BKG-03, FR-BKG-04): ช่วง 09.00 น. ว่าง 0 ที่"""
    from sqlalchemy import func, select

    from app.db.models import Booking

    # Given ยืนยันตัวตนแล้ว และช่วง 09.00 น. มีที่นั่งว่าง 0 ที่ (ขยับจาก 1 ที่ใน Given)
    slot = make_slot(start="09:00", remaining=0, capacity=1)

    # When POST /bookings ด้วย slot_id ของช่วง 09.00 น.
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then (1) ไม่สร้างรายการจอง (FR-BKG-03)
    count = db.scalar(select(func.count()).select_from(Booking).where(Booking.slot_id == slot.id))
    assert count == 0

    # Then (2) ตอบ 409 (plan ข้อ 4)
    assert res.status_code == 409

    # Then (3) remaining ของช่วงนั้นยังเป็น 0 ไม่ติดลบ (FR-BKG-04)
    db.refresh(slot)
    assert slot.remaining == 0
    # การเสนอ 3 ช่วงใกล้เคียงตรวจใน AC-BKG-03 ไม่ตรวจที่นี่


def test_TC_BKG_01_4_not_authenticated(client, db, make_slot):
    """TC-BKG-01-4 (AC-BKG-01 ทางผิด, IF-IDP-01): ยังไม่ยืนยันตัวตน"""
    from sqlalchemy import func, select

    from app.db.models import Booking

    # Given ยังไม่ยืนยันตัวตน (ไม่มีผลยืนยันตัวตนจากระบบยืนยันตัวตน) และช่วง 09.00 น. มีที่นั่งว่าง 1 ที่
    slot = make_slot(start="09:00", remaining=1)

    # When POST /bookings ด้วย slot_id ของช่วง 09.00 น. (ไม่ส่ง header Authorization)
    client.post("/bookings", json={"slot_id": slot.id})

    # Then (1) ไม่สร้างรายการจอง (IF-IDP-01)
    count = db.scalar(select(func.count()).select_from(Booking).where(Booking.slot_id == slot.id))
    assert count == 0

    # Then (2) remaining ของช่วงนั้นยังเป็น 1 (IF-IDP-01)
    db.refresh(slot)
    assert slot.remaining == 1

    # Then (3) รหัสตอบกลับและข้อความที่แจ้งผู้ใช้: ยังไม่ตรวจ เพราะ spec ไม่ได้บอก
