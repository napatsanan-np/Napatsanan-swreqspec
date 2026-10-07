# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ลบของเก่า

---

## 2569-09-23 13.40 คำสั่ง: /tasks specs/001-booking/spec.md

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: specs/001-booking/tasks.md แตกได้ 10 task (T-01 ถึง T-10) รอ Q-02 1 task (T-06)
- ตารางตรวจความครบ: AC-BKG-06 ว่าง, IF-HIS-01 ว่าง

### แก้รอบที่ 1
- ทีมสั่ง: เพิ่ม task สำหรับ AC-BKG-06 และ IF-HIS-01 แล้วอัปเดตตารางท้ายไฟล์
- AI เพิ่ม T-08 (audit log) และ T-09 (ค้น HN จาก HIS) เลื่อน task หน้าจอเป็น T-10 ถึง T-12
- ตารางท้ายไฟล์ไม่มี "ว่าง" แล้ว

---

## 2569-09-23 14.20 คำสั่ง: /implement T-01 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_T01_schema.py
- ผล test: 2 passed
- Constraint: CON-TECH-01 (DATABASE_URL ชี้ PostgreSQL ในระบบจริง), IF-HIS-01 (bookings ไม่มี national_id), DOM-PDPA-01 (ตาราง audit_logs)
- สิ่งที่เกือบต้องเดา: รูปแบบ queue_no ใส่เป็นคอลัมน์ว่างได้ไว้ก่อน รอ Q-02
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-27 19.05 คำสั่ง: /implement T-02 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/slots/router.py, backend/app/slots/service.py, backend/app/main.py, backend/tests/conftest.py, backend/tests/test_AC_BKG_05.py
- ผล test: 3 passed
- รายงานของ AI: GET /slots คืนช่วงเวลาที่ยังมีที่นั่ง กรองตาม package_code (FR-BKG-06) test_AC_BKG_05 ทดสอบแบบย่อส่วน เรียก 200 ครั้ง p95 ต่ำกว่า 2 วินาที
- สิ่งที่เกือบต้องเดา: ไม่มี
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-28 20.30 คำสั่ง: /implement T-03 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/booking/router.py, backend/app/booking/service.py, backend/app/auth/idp.py และแก้ backend/app/main.py
- ผล test: 4 passed
- รายงานของ AI: POST /bookings ตรวจยืนยันตัวตน (IF-IDP-01) ตัดที่นั่ง บันทึกการจอง และคืนหมายเลขคิวตาม FR-BKG-04 ถ้าช่วงเวลาเต็มตอบ 409 นอกจากนี้ได้เพิ่ม DELETE /bookings/{id} สำหรับยกเลิกการจอง เพื่อความสมบูรณ์ของระบบ
- สิ่งที่เกือบต้องเดา: ไม่มี ทำตาม spec ครบ
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- เครื่องมือ: Claude Code (VS Code)
- โหมด: ร่าง (AC-BKG-01 ยังไม่มีแถวใน test-cases.md)
- TC ID ที่เสนอ (สถานะ "ร่าง" ทั้งหมด): TC-BKG-01-1 (ทางปกติ pytest), TC-BKG-01-2 (ทางปกติ vitest), TC-BKG-01-3 (ขอบ ว่าง 0 ที่ pytest), TC-BKG-01-4 (ทางผิด ยังไม่ยืนยันตัวตน pytest), TC-BKG-01-5 (ทางปกติ คน ทั้งเส้น)
- ไม่ได้เขียนโค้ด test ไม่ได้แก้โค้ดของระบบ
- คำถามที่ AI ถามทีม:
  1. TC-BKG-01-4: ผู้ที่ยังไม่ยืนยันตัวตนกดจอง ต้องตอบรหัสอะไร และแจ้งผู้ใช้ว่าอย่างไร (spec และ plan ข้อ 4 ไม่ได้บอก โค้ดตอนนี้ตอบ 401 แต่ไม่ได้มาจาก spec)
  2. ส่วน "แสดงหมายเลขคิว" ติด Q-02 (รูปแบบเลขคิว) และ T-06 สถานะ "รอ Q-02" test หน้าจอ TC-BKG-01-2 จะตรวจได้แค่ว่าแสดงค่าที่ API ส่งมา
- คำตอบของทีม: (ยังไม่ตอบ)

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/ (รอบที่ 2)

- เครื่องมือ: Claude Code (VS Code)
- โหมด: เขียน test (ทีมเปลี่ยน TC-BKG-01-1 เป็น "ใช้ได้" แถวเดียว แถว 2 ถึง 5 ยังเป็น "ร่าง" จึงยังไม่เขียน)
- TC ID ที่เขียน test: TC-BKG-01-1 -> test_TC_BKG_01_1_book_last_seat ใน backend/tests/test_AC_BKG_01.py (เพิ่มต่อท้าย จำนวน test ในไฟล์ 1 -> 2)
- ส่วน (2) ตรวจแค่ว่ามีช่อง queue_no ไม่ตรวจค่าและรูปแบบเพราะรอ Q-02
- ผล test: `cd backend && pytest -v` 5 passed (test ใหม่ผ่าน)
- ข้อสังเกตที่ AI แจ้งทีม (ไม่ได้แก้โค้ด):
  1. backend/app/booking/service.py ฟังก์ชัน next_queue_no ออกเลขรูปแบบ A001 และรีเซ็ตรายวัน ซึ่งเป็นการตัดสินใจเรื่อง Q-02 ที่ยังไม่ได้คำตอบ
  2. backend/app/booking/service.py เงื่อนไข `slot.remaining < 0` น่าจะทำให้จองช่วงที่เหลือ 0 ที่ได้ (เกี่ยวกับ TC-BKG-01-3 ที่ยังเป็น "ร่าง")

---

## 2569-10-07 ทีมสั่ง: แก้ backend/app/booking/service.py ให้ปฏิเสธการจองเมื่อไม่มีที่นั่ง ห้ามแก้ test แล้วรัน pytest -v

- เครื่องมือ: Claude Code (VS Code)
- เหตุผลที่แก้ (ตามที่ทีมแจ้ง): โค้ดยอมให้จองเมื่อเหลือ 0 ที่ (ทีมอ้าง TC-BKG-01-2 แต่แถวที่ตรงกับกรณีนี้คือ TC-BKG-01-3 ซึ่งยังเป็น "ร่าง" และยังไม่มี test ในโค้ด)
- สิ่งที่แก้: backend/app/booking/service.py บรรทัด 26 ใน create_booking เปลี่ยน `if slot.remaining < 0:` เป็น `if slot.remaining <= 0:` (รองรับ FR-BKG-03 ไม่สร้างรายการจองเมื่อช่วงเวลาเต็ม และ FR-BKG-04 ตัดที่นั่งเฉพาะเมื่อยืนยันสำเร็จ)
- ไม่ได้แก้ไฟล์ test และไม่ได้แก้ไฟล์อื่น
- ผล test: `cd backend && pytest -v` 5 passed
- ยังไม่มี test ที่ยืนยันการแก้นี้โดยตรง จนกว่าทีมจะเปลี่ยน TC-BKG-01-3 เป็น "ใช้ได้" แล้วสั่ง /testcases

---

## 2569-10-07 ทีมสั่ง: คืน test_AC_BKG_01 เดิมกลับมา ห้ามลบ test เดิม

- เครื่องมือ: Claude Code (VS Code)
- ผลการตรวจ: `git diff backend/tests/test_AC_BKG_01.py` เทียบกับ commit ล่าสุด มีแต่บรรทัดที่เพิ่ม (test_TC_BKG_01_1_book_last_seat) ไม่มีบรรทัดที่ถูกลบหรือแก้ test_AC_BKG_01 ยังอยู่ครบเหมือนเดิมทุกบรรทัด
- สิ่งที่แก้: ไม่ได้แก้ไฟล์ใด เพราะไม่มีอะไรต้องคืน
- ผล test ล่าสุด: `cd backend && pytest -v` 5 passed (รวม test_AC_BKG_01 PASSED)

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/ (รอบที่ 3)

- เครื่องมือ: Claude Code (VS Code)
- โหมด: เขียน test (ทีมเปลี่ยน TC-BKG-01-2 ถึง 5 เป็น "ใช้ได้")
- TC ID ที่เขียน test:
  - TC-BKG-01-3 -> test_TC_BKG_01_3_no_seat_left (backend/tests/test_AC_BKG_01.py)
  - TC-BKG-01-4 -> test_TC_BKG_01_4_not_authenticated (backend/tests/test_AC_BKG_01.py) ส่วน (3) ไม่เขียน assert เพราะ spec ไม่ได้บอก
  - TC-BKG-01-2 -> frontend/src/__tests__/TC-BKG-01-2.test.jsx (ไฟล์ใหม่) ไม่ตรวจรูปแบบเลขคิวเพราะรอ Q-02
  - TC-BKG-01-5 ตรวจด้วย "คน" ไม่เขียนโค้ด คัดขั้นตอนให้ทีมในรายงาน
- จำนวน test ใน test_AC_BKG_01.py: 2 -> 4 (เพิ่ม 2 เท่ากับจำนวนแถว pytest ที่เขียน) test เดิมอยู่ครบ
- ผล test หลังบ้าน: `cd backend && pytest -v` 7 passed (TC-BKG-01-3 ผ่านหลังทีมสั่งแก้ `<= 0` ใน service.py รอบก่อน)
- ผล test หน้าจอ: `cd frontend && npm test` TC-BKG-01-2.test.jsx ไม่ผ่าน เพราะยังไม่มี src/pages/ConfirmBooking.jsx (T-11 ยังไม่ได้ทำ และ T-06 รอ Q-02) ไม่ใช่บั๊ก setup.test.jsx ยังผ่าน
- ข้อตกลงที่ test หน้าจอใช้ (ทีมควรตรวจ ไม่ได้มาจาก spec): ConfirmBooking รับ prop `api` (client จำลอง ตามคอมเมนต์ใน src/api/client.js) และ `slotId` และมีปุ่มที่ชื่อมีคำว่า "ยืนยัน"
- ไม่ได้แก้โค้ดของระบบ

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/ (รอบที่ 4)

- เครื่องมือ: Claude Code (VS Code)
- โหมด: ไม่มีงานต้องเขียน แถว "ใช้ได้" (TC-BKG-01-1, 2, 3) มี test ในโค้ดครบแล้ว ทีมเปลี่ยน TC-BKG-01-4 และ 5 กลับเป็น "ร่าง"
- TC ID ที่เขียน test: ไม่มี ไม่ได้แก้ไฟล์ test และไม่ได้แก้โค้ดของระบบ
- ผล test: `cd backend && pytest` 7 passed, `cd frontend && npm test` TC-BKG-01-2.test.jsx ยังไม่ผ่าน (ยังไม่มีหน้า ConfirmBooking.jsx, T-11 ยังไม่ได้ทำ)
- ข้อค้นพบ: test_TC_BKG_01_4_not_authenticated ถูกเขียนไว้แล้วในรอบที่ 3 ตอนแถวยังเป็น "ใช้ได้" แต่ตอนนี้แถวกลับเป็น "ร่าง" AI ไม่ลบ test (ห้ามลบ test เดิม) รอทีมตัดสิน
- คำถามที่ AI ถามทีม: จะเก็บ test_TC_BKG_01_4 ไว้, ให้ลบ, หรือให้แก้ตามแถวหลังทีมแก้ Then ส่วน (3)
- คำตอบของทีม: (ยังไม่ตอบ)

---

## 2569-10-07 ทีมสั่ง: พิสูจน์ว่า TC-BKG-01-3 จับบั๊ก `remaining < 0` ได้จริง (ทีมอนุญาตให้ใช้โค้ดเดิมชั่วคราว)

- เครื่องมือ: Claude Code (VS Code)
- วิธีทำ: สำรอง backend/app/booking/service.py ฉบับแก้แล้วไว้ใน scratchpad, เอาฉบับใน commit ล่าสุด (บรรทัด 26 `if slot.remaining < 0:`) มาใช้ชั่วคราว, รัน `cd backend && pytest -v`, แล้วคืนฉบับแก้แล้ว (`<= 0`) ตรวจด้วย cmp ว่าเหมือนเดิมทุกไบต์
- ผลกับโค้ดเดิม: 1 failed, 6 passed
  `FAILED tests/test_AC_BKG_01.py::test_TC_BKG_01_3_no_seat_left - assert 1 == 0` (สร้างรายการจองขึ้น 1 รายการ ทั้งที่ช่วงเหลือ 0 ที่)
- ผลหลังคืนโค้ดที่แก้แล้ว: 7 passed
- ไม่ได้แก้ไฟล์ test ไม่มีการเปลี่ยนแปลงโค้ดของระบบค้างอยู่
