# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 (เพิ่มหมวด "หน้าจอ (UI)" v3 2569-10-07) | tasks.md (เสร็จ T-01 ถึง T-03, เสร็จ รอทีมตรวจ T-10 และ T-11) | test-cases.md (AC-BKG-01 5 แถว) | mockups/UI-BKG-01, UI-BKG-02
สร้างด้วย /verify เมื่อ 2569-10-07 09.17 (รอบที่ 2) | test: 10 ผ่าน 1 ไม่ผ่าน (หลังบ้าน 7 ผ่าน 0 ไม่ผ่าน, หน้าจอ 3 ผ่าน 1 ไม่ผ่าน)

ผล test ที่รัน
- `cd backend && pytest -v`: test_AC_BKG_01, test_TC_BKG_01_1_book_last_seat, test_TC_BKG_01_3_no_seat_left, test_TC_BKG_01_4_not_authenticated, test_AC_BKG_05, test_T01_tables_created, test_T01_no_national_id ผ่านทั้งหมด
- `cd frontend && npm test`: AC-BKG-03.test.jsx ผ่าน, SlotPicker.test.jsx ผ่าน, setup.test.jsx ผ่าน, TC-BKG-01-2.test.jsx ไม่ผ่าน (`TypeError: Cannot read properties of undefined (reading 'slot_date')` test ส่ง prop `slotId` ที่ AI สมมติไว้ตอนยังไม่มีหน้า แต่หน้าจริงรับ prop `slot` และหน้า BookingResult ของ T-06 ยังรอ Q-02)
- หมายเหตุ: AC-BKG-03.test.jsx และ ConfirmBooking.jsx มีการแก้ที่ยังไม่ commit ผลข้างบนรันจาก working tree ปัจจุบัน
- ไม่มีโฟลเดอร์ specs/000-shared/ และ plan.md ไม่มีตาราง "ค่าที่ตั้งได้" จึงยังไม่ตรวจชนิด "ตัวเลขฝังในโค้ด"

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 (ตรวจแค่ความเร็ว) | T-02 เสร็จ, T-10 เสร็จ รอทีมตรวจ | backend/app/slots/service.py: list_available_slots, backend/app/slots/router.py: get_slots, frontend/src/pages/SlotPicker.jsx | ไม่มี test ตรวจช่วง 30 วัน การแสดงแต่ละวัน หรือคำว่า "เหลือ N ที่" | ช่องโหว่ (F-04, F-06, F-12, F-16, F-17, F-18, F-23) |
| FR-BKG-02 | AC-BKG-02 | T-04 พร้อมทำ | ยังไม่มี | ยังไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-11 เสร็จ รอทีมตรวจ, T-05 และ T-12 พร้อมทำ | frontend/src/pages/ConfirmBooking.jsx (แจ้ง "ช่วงเวลาเต็ม" แสดง 3 ตัวเลือก), backend ตอบ 409 แต่ยังไม่ส่ง alternatives (T-05) | AC-BKG-03.test.jsx (ผ่าน) ส่วน "ไม่มีรายการจองซ้อน" และ "ใกล้ 09.00 น. ที่สุด" รอ T-05 | ช่องโหว่ (F-21) |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ, T-11 เสร็จ รอทีมตรวจ, T-06 รอ Q-02 | backend/app/booking/service.py: create_booking, next_queue_no, backend/app/booking/router.py: create_booking, frontend/src/pages/ConfirmBooking.jsx: confirm | test_AC_BKG_01 (ผ่าน), test_TC_BKG_01_1 (ผ่าน), test_TC_BKG_01_3 (ผ่าน), TC-BKG-01-2.test.jsx (ไม่ผ่าน ดูหมายเหตุผล test) ส่วน "ส่งคำขอส่งข้อความยืนยัน" รอ T-07 | ช่องโหว่ (F-05, F-11, F-15) |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ยังไม่มี | ยังไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02 เสร็จ, T-10 เสร็จ รอทีมตรวจ | backend/app/slots/service.py: list_available_slots (กรอง package_code), frontend/src/pages/SlotPicker.jsx: useEffect โหลดใหม่เมื่อเปลี่ยนแพ็กเกจ | SlotPicker.test.jsx (ผ่าน ไม่ได้อ้าง AC) | ช่องโหว่ (F-07, F-20) |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ | backend/app/slots/service.py: list_available_slots | test_AC_BKG_05 (ผ่าน แบบย่อส่วน ทีมตัดสิน F-10 ว่าไม่ใช่ปัญหา) | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี | ไม่มี | ช่องโหว่ (F-08) |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ยังไม่มี | ยังไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่เกี่ยวกับโค้ดโดยตรง | ไม่มี | ช่องโหว่ (F-09) |
| CON-TECH-01 | ไม่มี AC | T-01 เสร็จ | backend/app/config.py: DATABASE_URL, backend/app/db/session.py, backend/requirements.txt: psycopg | test_T01_tables_created (ผ่าน บน SQLite ทีมตัดสิน F-14 ว่าไม่ใช่ปัญหา) | ครบ |
| DOM-PDPA-01 | AC-BKG-06 | T-01 เสร็จ (ตาราง), T-08 พร้อมทำ | มีแค่ backend/app/db/models.py: AuditLog | test_T01_tables_created ตรวจแค่ว่ามีตาราง | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC ตรง (TC-BKG-01-4 สถานะ "ร่าง") | T-03 เสร็จ | backend/app/auth/idp.py: get_verified_hn | test_TC_BKG_01_4_not_authenticated (ผ่าน แต่แถวยังเป็น "ร่าง") | ช่องโหว่ (F-13) |
| IF-HIS-01 | ไม่มี AC | T-01 เสร็จ, T-09 พร้อมทำ | backend/app/db/models.py: Booking (ไม่มี national_id) | test_T01_no_national_id (ผ่าน) | ช่องโหว่ (F-01) |
| IF-NOT-01 | ไม่มี AC ตรง (AC-BKG-04 เกี่ยวข้อง) | T-07 พร้อมทำ | ยังไม่มี | ยังไม่มี | ยังไม่ถึง |

สรุป: ครบ 2 | ยังไม่ถึง 5 | รอ 0 | ช่องโหว่ 8 (รวม 15 แถว)

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/router.py: GET /slots | FR-BKG-01, FR-BKG-06 | ตรงบางส่วน | ช่วงวันที่ไม่ตรง (F-04) response ใช้ชื่อ `slot_id` แต่ SlotPicker อ่าน `s.id` จะไม่ตรงกันเมื่อทำ T-12 (ยังไม่ถึง) |
| backend/app/slots/service.py: list_available_slots, DAYS_AHEAD | FR-BKG-01, FR-BKG-06 | ไม่ตรง | 14 วันแทน 30 วัน (F-04), `date.today()` ไม่ใช่ Asia/Bangkok (F-12) |
| backend/app/booking/router.py: POST /bookings | FR-BKG-04, IF-IDP-01 | ตรงบางส่วน | รับ `national_id` และเขียนลง log (F-01) |
| backend/app/booking/router.py: DELETE /bookings/{booking_id} | FR-BKG-04 | ไม่ตรง | อยู่ใน Out of scope (F-02, F-03) |
| backend/app/booking/service.py: create_booking | FR-BKG-04 | ตรง | ตรวจที่นั่ง (`<= 0`), ตัดที่นั่ง, บันทึก |
| backend/app/booking/service.py: next_queue_no | FR-BKG-04 | ไม่ตรง | เดา Q-02 (F-05) |
| backend/app/booking/service.py: cancel_booking | FR-BKG-04 | ไม่ตรง | อยู่ใน Out of scope (F-02, F-03) |
| backend/app/auth/idp.py: get_verified_hn | IF-IDP-01 | ตรง | ตัวจำลองระบบยืนยันตัวตน |
| backend/app/db/models.py, session.py, config.py, migrations/001_init.py, main.py | CON-TECH-01, DOM-PDPA-01, IF-HIS-01 | ตรง | |
| frontend/src/App.jsx: App | T-10, T-11 | ไม่ตรง | ส่ง slot_date เป็นวันนี้และ start_time `'09:00'` ตายตัว ไม่ใช่ช่วงที่ผู้ใช้เลือก (F-16) วันนี้คิดแบบ UTC (F-23) |
| frontend/src/pages/SlotPicker.jsx: SlotPicker | FR-BKG-01, FR-BKG-06, UI-BKG-01 | ตรงบางส่วน | ช่องแพ็กเกจอยู่บนสุดและแถบ 3 ขั้นตรง แต่ไม่มีการเลือกวัน (F-17) ข้อความ "ว่าง N" ไม่ใช่ "เหลือ N ที่" (F-18) รายการแพ็กเกจฝังในโค้ด (F-20) ปุ่ม "ถัดไป" เป็นปุ่มนำทาง ไม่ต้องมี FR |
| frontend/src/pages/ConfirmBooking.jsx: ConfirmBooking | FR-BKG-03, FR-BKG-04, UI-BKG-02 | ตรงบางส่วน | ปุ่ม "ยืนยันการจอง" ข้อความ "ช่วงเวลาเต็ม" และ 3 ตัวเลือกพร้อมวันเวลาตรง UI-BKG-02 แล้ว ปุ่มยกเลิกถูกลบแล้ว แต่ถือทุกผลที่ไม่ใช่ 409 เป็น "จองสำเร็จ" (F-15) ปุ่ม "กลับไปเลือกเวลา" เป็นปุ่มนำทาง สถานะ "จองเพิ่มไม่ได้" ของ AC-BKG-02 ยังไม่มีเพราะ T-04 ยังไม่ทำ |
| frontend/src/api/client.js: getSlots, createBooking | plan ข้อ 4 | ตรงบางส่วน | createBooking ยังไม่ส่ง header Authorization (IF-IDP-01) รอ T-12 |
| frontend/src/api/client.js: cancelBooking | ไม่มี (คอมเมนต์ "เพิ่มตอนทำ T-11") | ไม่ตรง | อยู่ใน Out of scope (F-19) |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง / ไม่ตรง mockup / mockup เกิน spec
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | ละเมิด Constraint | backend/app/booking/router.py บรรทัด 19, 25 | IF-HIS-01 | POST /bookings รับช่อง `national_id` และ `logger.info` เขียนเลขบัตรประชาชนลง log ทุกครั้งที่จอง IF-HIS-01 ให้อ้างอิงด้วย HN และไม่เก็บเลขบัตร การค้น HN ใน plan ข้อ 4 อยู่ที่ GET /patients/lookup วิธีแก้ที่น่าจะเป็น: ลบช่อง national_id ออกจาก BookingRequest และออกจาก log ไม่มี test ที่จับเรื่องนี้ (test_T01_no_national_id ตรวจแค่ตาราง) | แก้โค้ด: IF-HIS-01 ห้ามเก็บเลขบัตรประชาชน ลบ national_id ออกจาก BookingRequest และออกจาก log |
| F-02 | โค้ดไม่มี FR | backend/app/booking/router.py บรรทัด 35-41: DELETE /bookings/{booking_id}, backend/app/booking/service.py บรรทัด 42-50: cancel_booking | Out of scope (ยกเลิก / เลื่อนคิว UC-02) | การยกเลิกคิวอยู่ใน Out of scope ไม่มีใน plan ข้อ 4 และไม่มี task รองรับ prompt-log ของ /implement T-03 บันทึกว่า AI เพิ่มเอง "เพื่อความสมบูรณ์ของระบบ" endpoint นี้คืนที่นั่งได้ด้วย ไม่มี test | แก้โค้ด: ของแถม อยู่ใน Out of scope (UC-02) ลบ endpoint DELETE /bookings/{id} และ cancel_booking ออก |
| F-03 | อ้าง ID ผิดเรื่อง | backend/app/booking/router.py บรรทัด 37, backend/app/booking/service.py บรรทัด 43 | FR-BKG-04 | คอมเมนต์ของ cancel_booking อ้าง FR-BKG-04 แต่ FR-BKG-04 พูดถึง "เมื่อยืนยันสำเร็จ ระบบต้องบันทึกการจอง ตัดจำนวนที่นั่ง ออกหมายเลขคิว" ไม่ได้พูดถึงการยกเลิกหรือคืนที่นั่ง | แก้โค้ด: ลบไปพร้อมกับ F-02 คอมเมนต์ที่อ้าง FR-BKG-04 ผิดจะหายไปด้วย |
| F-04 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py บรรทัด 10: `DAYS_AHEAD = 14` | FR-BKG-01, Scope (30 วันข้างหน้า) | GET /slots คืนช่วงเวลาแค่ 14 วัน ทั้งที่ spec บอก 30 วัน ผู้ใช้จะไม่เห็นช่วงวันที่ 15 ถึง 30 test ไม่จับได้ เพราะไม่มี AC ตรวจเรื่องนี้ (ดู F-06) | แก้โค้ด: FR-BKG-01 และ Scope บอก 30 วัน เปลี่ยน DAYS_AHEAD เป็น 30 |
| F-05 | เดา Q-02 | backend/app/booking/service.py บรรทัด 13-18: next_queue_no | Q-02 (ยังไม่มีคำตอบ), plan ข้อ 1 และข้อ 8 | โค้ดออกเลขคิวรูปแบบ `A001` และเริ่มนับใหม่ทุกวัน ทั้งที่ Q-02 ยังรอเจ้าหน้าที่เวชระเบียน และ A001 คือตัวอย่างในวงเล็บของ Q-02 plan บอกว่า "ยังไม่กำหนดวิธีออกเลข" และ T-06 สถานะ "รอ Q-02" (models.py ก็เขียนว่า queue_no รอ Q-02) | แก้โค้ด: Q-02 ยังไม่มีคำตอบ ห้ามใช้ตัวอย่าง A001 เป็นคำตอบ ให้ queue_no ว่างไว้ตาม plan ข้อ 3 จนกว่าเวชระเบียนจะตอบ |
| F-06 | FR ไม่มี AC | spec.md: FR-BKG-01 | FR-BKG-01 | FR-BKG-01 บอกให้แสดงช่วงเวลาที่ว่างภายใน 30 วันพร้อมจำนวนที่นั่งคงเหลือ แต่ AC เดียวที่อ้าง (AC-BKG-05) ตรวจแค่ความเร็ว ทำให้ไม่มีใครจับ F-04 ได้ ควรเสนอ AC เช่น ลองวันที่ 30 และ 31 | แก้ spec: เพิ่ม AC ของ FR-BKG-01 ที่ตรวจช่วงวันที่ 30 (แสดง) และ 31 (ไม่แสดง) พร้อมที่นั่งคงเหลือ |
| F-07 | FR ไม่มี AC | spec.md: FR-BKG-06 | FR-BKG-06 | FR-BKG-06 (เปลี่ยนแพ็กเกจแล้วคำนวณช่วงว่างใหม่) ไม่มี AC เลย plan ข้อ 6 ก็บันทึกไว้แล้วว่า "ควรเสนอทีมเพิ่ม AC" โค้ดกรองด้วย package_code มีอยู่แล้วแต่ไม่มี test | แก้ spec: เพิ่ม AC ของ FR-BKG-06 (เปลี่ยนแพ็กเกจแล้วช่วงเวลาเปลี่ยนตาม) ตามที่ plan ข้อ 6 เสนอไว้ |
| F-08 | FR ไม่มี AC | spec.md: NFR-SEC-01 | NFR-SEC-01 | ไม่มี AC ไม่มี task ใน tasks.md และ plan ไม่ได้พูดถึง TLS 1.2 เลย ไม่มีใครรับผิดชอบข้อนี้ | แก้ spec: เพิ่ม AC ของ NFR-SEC-01 แล้วให้ /tasks เพิ่ม task ตั้งค่า TLS 1.2 ขึ้นไป |
| F-09 | FR ไม่มี AC | spec.md: NFR-USE-01 | NFR-USE-01 | ไม่มี AC ไม่มี task และไม่มีแผนทดสอบกับอาสาสมัคร 10 คน (ASM-05) ทั้งใน plan ข้อ 6 และ test-cases.md | แก้ spec: เพิ่ม AC ของ NFR-USE-01 ทดสอบกับอาสาสมัคร 10 คนตาม ASM-05 ตรวจด้วย "คน" |
| F-10 | test อ่อน | backend/tests/test_AC_BKG_05.py | AC-BKG-05, NFR-PERF-01 | Given ของ AC คือ "ผู้ใช้พร้อมกัน 200 คน" แต่ test เรียก 200 ครั้งต่อกันทีละครั้ง (ไม่พร้อมกัน) บน SQLite ในหน่วยความจำและมีแค่ 10 ช่วง ส่วน "พร้อมกัน 200 คน" จึงไม่มี assert plan ข้อ 6 บอกไว้แล้วว่าผลจริงต้องวัดบนเครื่องทดสอบ แต่ยังไม่มี task หรือแถว "คน" สำหรับการวัดนั้น | ไม่ใช่ปัญหา: plan ข้อ 6 ตั้งใจทดสอบแบบย่อส่วนใน Codespace ผลจริงต้องวัดบนเครื่องทดสอบ |
| F-11 | test อ่อน | backend/tests/test_AC_BKG_01.py: test_AC_BKG_01 | AC-BKG-01 | test ชื่ออ้าง AC-BKG-01 แต่ assert แค่ `status_code == 201` ไม่ดูผลในข้อมูล ผลกระทบต่ำ เพราะ test_TC_BKG_01_1 ตรวจบันทึกและ remaining แล้ว ส่วน "แสดงหมายเลขคิว" ยังรอ T-06 / Q-02 | ไม่ใช่ปัญหา: test_TC_BKG_01_1 ตรวจบันทึกและ remaining ครบแล้ว test เดิมห้ามลบจึงคงไว้ |
| F-12 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py บรรทัด 15: `date.today()` | ASM-02 | วันเริ่มนับใช้เขตเวลาของเครื่องที่รัน ไม่ได้กำหนด Asia/Bangkok ตาม ASM-02 ถ้าเครื่องตั้งเป็น UTC ช่วงเวลา 00.00 ถึง 07.00 น. จะนับวันผิดไป 1 วัน | แก้โค้ด: ASM-02 กำหนดให้ "วันเดียวกัน" ใช้เขตเวลา Asia/Bangkok ให้นับวันด้วยเขตเวลานี้ |
| F-13 | FR ไม่มี AC | backend/tests/test_AC_BKG_01.py: test_TC_BKG_01_4_not_authenticated, test-cases.md TC-BKG-01-4 | IF-IDP-01 | IF-IDP-01 ไม่มี AC ตรง ที่ตรวจอยู่คือแถว TC-BKG-01-4 ซึ่งทีมเปลี่ยนกลับเป็น "ร่าง" แล้ว แต่ test ในโค้ดยังอยู่และผ่าน ตารางกับโค้ดจึงไม่ตรงกัน และ Then ส่วน (3) (รหัสตอบกลับเมื่อยังไม่ยืนยันตัวตน) ยัง "spec ไม่ได้บอก" | เพิ่ม Q-xx: spec ไม่ได้บอกว่าถ้ายังไม่ยืนยันตัวตนต้องตอบอะไร ถามแล้วค่อยแก้ Then (3) และอนุมัติ TC-BKG-01-4 ใหม่ |
| F-14 | FR ไม่มี AC | backend/tests/test_T01_schema.py | CON-TECH-01 | ไม่มี AC และ test ทั้งหมดรันบน SQLite ตามที่ plan ตั้งใจ ยังไม่เคยมีการตรวจว่า migration และ query ทำงานบน PostgreSQL จริง ทีมอาจตัดสินว่า "ไม่ใช่ปัญหา" ถ้ายอมรับตาม plan ข้อ 2 | ไม่ใช่ปัญหา: plan ข้อ 2 ตั้งใจใช้ SQLite ตอน test ระบบจริงต่อ PostgreSQL ผ่าน DATABASE_URL |
| F-15 | ตัวเลขไม่ตรง spec | frontend/src/pages/ConfirmBooking.jsx บรรทัด 11: `else { setBooking(res.body) ... }` | FR-BKG-04, IF-IDP-01 | เงื่อนไขในหน้าจอ: ผลทุกแบบที่ไม่ใช่ 409 (เช่น 401 ยังไม่ยืนยันตัวตน หรือ 404 ไม่พบช่วงเวลา) ถูกแสดงเป็น "จองสำเร็จ หมายเลขคิว undefined" FR-BKG-04 ให้แสดงผลเมื่อ "ยืนยันสำเร็จ" เท่านั้น และตอนนี้ client.js ยังไม่ส่ง Authorization หลังบ้านจึงจะตอบ 401 ทุกครั้งเมื่อต่อจริง วิธีแก้ที่น่าจะเป็น: แสดง "จองสำเร็จ" เฉพาะเมื่อ status 201 ไม่มี test ที่จับเรื่องนี้ | |
| F-16 | ตัวเลขไม่ตรง spec | frontend/src/App.jsx บรรทัด 15: `setSlot({ id, slot_date: today, start_time: '09:00' })` | FR-BKG-04, UI-BKG-02 | หน้าเลือกเวลาส่งแค่ id กลับมา App เลยเติมวันที่เป็นวันนี้และเวลาเป็น 09.00 น. ตายตัว หน้ายืนยันจึงแสดงวันเวลาที่ผู้ใช้ไม่ได้เลือก (เลือก 13.00 น. ก็ขึ้น 09.00 น.) ในขณะที่ slot_id ที่จองจริงคือช่วงที่เลือก ผู้ใช้จะยืนยันโดยเห็นข้อมูลผิด | |
| F-17 | ไม่ตรง mockup | frontend/src/pages/SlotPicker.jsx | FR-BKG-01, UI-BKG-01 | FR-BKG-01 ให้แสดงช่วงว่าง "ของแต่ละวันภายใน 30 วัน" และ mockup มีแถว "วันที่ (ภายใน 30 วันข้างหน้า)" (data-req FR-BKG-01) แต่หน้าจอไม่มีการเลือกวัน และรายการแสดงแค่เวลา ไม่บอกวัน ถ้า API คืนหลายวัน ผู้ใช้จะแยกไม่ออก (spec ให้หน้าตาปุ่มเลือกวันยืดหยุ่นได้ แต่ต้องมีการแยกตามวัน) | |
| F-18 | ไม่ตรง mockup | frontend/src/pages/SlotPicker.jsx บรรทัด 46: `ว่าง {s.remaining}` | UI-BKG-01 "ต้องตรง" | spec ระบุว่าต้องแสดงคำว่า "เหลือ N ที่" แต่หน้าจอแสดง "ว่าง N" SlotPicker.test.jsx ไม่ได้ตรวจข้อความนี้ | |
| F-19 | โค้ดไม่มี FR | frontend/src/api/client.js บรรทัด 20-24: cancelBooking | Out of scope (ยกเลิก / เลื่อนคิว UC-02) | ฟังก์ชันเรียก DELETE /bookings/{id} อยู่ใน Out of scope คอมเมนต์บอกว่าเพิ่มตอนทำ T-11 เพื่อปุ่มยกเลิก ซึ่งปุ่มถูกลบไปแล้ว ตอนนี้จึงไม่มีใครเรียกใช้ คู่กับ F-02 ฝั่งหลังบ้าน | |
| F-20 | ตัวเลขไม่ตรง spec | frontend/src/pages/SlotPicker.jsx บรรทัด 4-7: `PACKAGES` | FR-BKG-06, UI-BKG-01 (ข้อมูลตัวอย่างทั้งหมดยืดหยุ่นได้) | รายการแพ็กเกจ (GEN "ตรวจสุขภาพทั่วไป", PRE "ตรวจสุขภาพก่อนเข้าทำงาน") ฝังในโค้ด โดยหยิบชื่อมาจากข้อมูลตัวอย่างใน mockup spec และ plan ข้อ 4 ไม่ได้บอกว่ารายการแพ็กเกจมาจากไหน และ test หลังบ้านใช้รหัส BASIC เมื่อต่อ API จริงอาจไม่มีช่วงเวลาให้เลือก เป็นการตัดสินใจแทนทีม | |
| F-21 | test อ่อน | frontend/src/__tests__/AC-BKG-03.test.jsx | AC-BKG-03, UI-BKG-02 | test ตรวจข้อความ "ช่วงเวลาเต็ม" และนับ 3 ปุ่ม แต่ไม่ assert ว่าแต่ละตัวเลือกแสดงวันและเวลา (UI-BKG-02 "แสดง 3 ตัวเลือกพร้อมวันและเวลา") และ API จำลองส่งมาพอดี 3 ตัว ถ้าลบ `.slice(0, 3)` test ก็ยังผ่าน ควรให้ API จำลองส่งเกิน 3 ตัว นอกจากนี้ assert ที่เข้มขึ้นยังเป็นการแก้ที่ยังไม่ commit ฉบับใน commit ล่าสุดตรวจแค่ "เต็ม" และจำนวนมากกว่า 0 | |
| F-22 | mockup เกิน spec | specs/001-booking/mockups/UI-BKG-01-select-slot.html: ช่อง "แจ้งเตือนก่อนวันตรวจ 1 วัน" | spec (ไม่มี FR) | mockup มีช่องติ๊ก "แจ้งเตือนก่อนวันตรวจ 1 วัน" ไม่มี data-req และไม่มี FR หรือ "ต้องตรง" รองรับ โค้ดไม่ได้ทำ (ถูกแล้ว) ทีมควรถามผู้ใช้หรือ PO ว่าต้องการหรือไม่ ถ้าต้องการให้เพิ่ม FR ก่อน ห้ามนับเป็นงานที่ขาด | |
| F-23 | ตัวเลขไม่ตรง spec | frontend/src/App.jsx บรรทัด 9: `new Date().toISOString().slice(0, 10)` | ASM-02 | วันเริ่มค้นหาคิดเป็นวันที่แบบ UTC ไม่ใช่ Asia/Bangkok ช่วง 00.00 ถึง 07.00 น. ตามเวลาไทยจะได้วันของเมื่อวาน คู่กับ F-12 ฝั่งหลังบ้าน | |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| (ยังไม่มี F-ID ที่แก้แล้ว) | F-01 ถึง F-14 ยังเจออยู่ทุกข้อ โค้ดหลังบ้านไม่เปลี่ยนตั้งแต่ commit "verify v1" ส่วนที่แก้ไปก่อนมี F-ID: บั๊ก `slot.remaining < 0` (แก้เป็น `<= 0`) และปุ่ม "ยกเลิกการจอง" ข้อความ "เต็มแล้ว" และ `.slice(0, 2)` ใน ConfirmBooking.jsx (ทีมสั่งแก้ 2569-10-07) | `git diff d31361b -- backend/app` ว่าง, test_TC_BKG_01_3 ผ่าน, ConfirmBooking.jsx ไม่มีคำว่า "ยกเลิก" แล้ว และ AC-BKG-03.test.jsx ผ่าน |
