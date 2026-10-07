// TC-BKG-01-2 (AC-BKG-01, FR-BKG-04): หน้าจอแสดงหมายเลขคิวที่ได้จาก API
// ใช้ API จำลองตามสัญญาใน plan.md ข้อ 4 (POST /bookings ตอบ booking id และ queue_no)
// หน้า ConfirmBooking รับ client จำลองผ่าน prop api ตามคอมเมนต์ใน src/api/client.js
import { fireEvent, render, screen } from '@testing-library/react'
import ConfirmBooking from '../pages/ConfirmBooking.jsx'

test('TC-BKG-01-2 แสดงหมายเลขคิวที่ได้จาก API', async () => {
  // Given API จำลองตอบการจองสำเร็จ พร้อม booking id และ queue_no
  const queueNo = 'QUEUE-FROM-API'
  const api = {
    createBooking: vi.fn().mockResolvedValue({
      status: 201,
      body: { booking_id: 1, slot_id: 10, queue_no: queueNo },
    }),
  }
  render(<ConfirmBooking api={api} slotId={10} />)

  // When ผู้ใช้กดยืนยันการจองบนหน้าจอ
  fireEvent.click(screen.getByRole('button', { name: /ยืนยัน/ }))

  // Then หน้าจอแสดงหมายเลขคิวที่ได้จาก API (FR-BKG-04, plan ข้อ 4 หน้า BookingResult)
  expect(await screen.findByText(queueNo, { exact: false })).toBeTruthy()
  // ยังไม่ตรวจรูปแบบของหมายเลขคิว เพราะรอ Q-02
})
