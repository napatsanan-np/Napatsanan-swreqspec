# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | tasks.md (เสร็จ T-01 ถึง T-03) | test-cases.md (AC-BKG-01 5 แถว)
สร้างด้วย /verify เมื่อ 2569-10-07 08.55 | test: 8 ผ่าน 1 ไม่ผ่าน (หลังบ้าน 7 ผ่าน 0 ไม่ผ่าน, หน้าจอ 1 ผ่าน 1 ไฟล์ไม่ผ่าน)

ผล test ที่รัน
- `cd backend && pytest -v`: test_AC_BKG_01, test_TC_BKG_01_1_book_last_seat, test_TC_BKG_01_3_no_seat_left, test_TC_BKG_01_4_not_authenticated, test_AC_BKG_05, test_T01_tables_created, test_T01_no_national_id ผ่านทั้งหมด
- `cd frontend && npm test`: setup.test.jsx ผ่าน, TC-BKG-01-2.test.jsx ไม่ผ่าน เพราะยังไม่มี src/pages/ConfirmBooking.jsx (T-06 รอ Q-02, T-11 ยังไม่ได้ทำ) ไม่ใช่บั๊ก

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 (ตรวจแค่ความเร็ว) | T-02 เสร็จ, T-10 พร้อมทำ | backend/app/slots/service.py: list_available_slots, backend/app/slots/router.py: get_slots | ไม่มี test ตรวจช่วง 30 วันหรือจำนวนที่นั่งคงเหลือ (test_AC_BKG_05 ผ่าน แต่ตรวจแค่ความเร็ว) | ช่องโหว่ (F-04, F-06, F-12) |
| FR-BKG-02 | AC-BKG-02 | T-04 พร้อมทำ | ยังไม่มี | ยังไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 พร้อมทำ | มีบางส่วน: backend/app/booking/router.py: create_booking ตอบ 409 "ช่วงเวลาเต็ม" แต่ยังไม่เสนอ 3 ช่วง | ยังไม่มี test ของ AC-BKG-03 | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ, T-06 รอ Q-02 | backend/app/booking/service.py: create_booking, next_queue_no, backend/app/booking/router.py: create_booking | test_AC_BKG_01 (ผ่าน), test_TC_BKG_01_1 (ผ่าน), test_TC_BKG_01_3 (ผ่าน), TC-BKG-01-2.test.jsx (ไม่ผ่าน ยังไม่มีหน้า) ส่วน "ส่งคำขอส่งข้อความยืนยัน" ยังไม่มี (T-07) | ช่องโหว่ (F-05, F-11) |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ยังไม่มี | ยังไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02 เสร็จ, T-10 พร้อมทำ | backend/app/slots/service.py: list_available_slots (กรอง package_code) | ไม่มี | ช่องโหว่ (F-07) |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ | backend/app/slots/service.py: list_available_slots | test_AC_BKG_05 (ผ่าน แบบย่อส่วน ไม่พร้อมกัน) | ช่องโหว่ (F-10) |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี (ไม่มีการตั้งค่า TLS ใน plan หรือโค้ด) | ไม่มี | ช่องโหว่ (F-08) |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ยังไม่มี | ยังไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่เกี่ยวกับโค้ดโดยตรง (ต้องทดสอบกับคน) | ไม่มี | ช่องโหว่ (F-09) |
| CON-TECH-01 | ไม่มี AC | T-01 เสร็จ | backend/app/config.py: DATABASE_URL, backend/app/db/session.py: engine, backend/requirements.txt: psycopg | test_T01_tables_created (ผ่าน บน SQLite เท่านั้น) | ช่องโหว่ (F-14) |
| DOM-PDPA-01 | AC-BKG-06 | T-01 เสร็จ (ตาราง), T-08 พร้อมทำ | มีบางส่วน: backend/app/db/models.py: AuditLog ยังไม่มีโค้ดที่เขียน audit log | test_T01_tables_created ตรวจแค่ว่ามีตาราง audit_logs | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC ตรง (TC-BKG-01-4 ใต้ AC-BKG-01 สถานะ "ร่าง") | T-03 เสร็จ | backend/app/auth/idp.py: get_verified_hn | test_TC_BKG_01_4_not_authenticated (ผ่าน แต่แถวยังเป็น "ร่าง") | ช่องโหว่ (F-13) |
| IF-HIS-01 | ไม่มี AC | T-01 เสร็จ, T-09 พร้อมทำ | backend/app/db/models.py: Booking (ไม่มี national_id) | test_T01_no_national_id (ผ่าน) | ช่องโหว่ (F-01) |
| IF-NOT-01 | ไม่มี AC ตรง (AC-BKG-04 เกี่ยวข้อง) | T-07 พร้อมทำ | ยังไม่มี | ยังไม่มี | ยังไม่ถึง |

สรุป: ครบ 0 | ยังไม่ถึง 6 | รอ 0 | ช่องโหว่ 9 (รวม 15 แถว)

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/router.py: GET /slots | FR-BKG-01, FR-BKG-06 | ตรงบางส่วน | ตรงกับ plan ข้อ 4 แต่ช่วงวันที่ไม่ตรง (F-04) |
| backend/app/slots/service.py: list_available_slots, DAYS_AHEAD | FR-BKG-01, FR-BKG-06 | ไม่ตรง | `DAYS_AHEAD = 14` แต่ FR-BKG-01 บอก 30 วัน (F-04), `date.today()` ใช้เขตเวลาของเครื่อง ไม่ใช่ Asia/Bangkok ตาม ASM-02 (F-12) |
| backend/app/booking/router.py: POST /bookings | FR-BKG-04, IF-IDP-01 | ตรงบางส่วน | ตรงกับ plan ข้อ 4 แต่ request รับ `national_id` และเขียนลง log (F-01) |
| backend/app/booking/router.py: BookingRequest.national_id | ไม่มี (คอมเมนต์ "เผื่อใช้ค้น HN จาก HIS") | ไม่ตรง | ขัด IF-HIS-01 การค้น HN ใน plan ข้อ 4 คือ GET /patients/lookup ไม่ใช่ POST /bookings (F-01) |
| backend/app/booking/router.py: logger.info ใน create_booking | ไม่มี | ไม่ตรง | log มีเลขบัตรประชาชน (F-01) |
| backend/app/booking/router.py: DELETE /bookings/{booking_id} | FR-BKG-04 | ไม่ตรง | ยกเลิกคิว (UC-02) อยู่ใน Out of scope ไม่มีใน plan ข้อ 4 และไม่มี task (F-02, F-03) |
| backend/app/booking/service.py: create_booking | FR-BKG-04 | ตรง | ตรวจที่นั่ง (`<= 0` แก้แล้วตามที่ทีมสั่ง), ตัดที่นั่ง, บันทึกการจอง |
| backend/app/booking/service.py: next_queue_no | FR-BKG-04 | ไม่ตรง | ออกเลขแบบ A001 รีเซ็ตรายวัน เป็นเรื่องของ Q-02 ที่ยังไม่มีคำตอบ และ A001 คือตัวอย่างในวงเล็บของ Q-02 (F-05) |
| backend/app/booking/service.py: cancel_booking | FR-BKG-04 | ไม่ตรง | อยู่ใน Out of scope (F-02, F-03) |
| backend/app/booking/service.py: SlotFullError | FR-BKG-03 (ทางอ้อม) | ตรงบางส่วน | ไม่สร้างรายการจองเมื่อเต็ม แต่ยังไม่เสนอ 3 ช่วง (T-05 ยังไม่ทำ) |
| backend/app/auth/idp.py: get_verified_hn | IF-IDP-01 | ตรง | เป็นตัวจำลองระบบยืนยันตัวตน ตามที่คอมเมนต์บอก |
| backend/app/db/models.py: Slot, Booking, AuditLog | CON-TECH-01, DOM-PDPA-01, IF-HIS-01, FR-BKG-04 | ตรง | ตรงกับ plan ข้อ 3 Booking ไม่มี national_id |
| backend/app/db/session.py, backend/app/config.py | CON-TECH-01 | ตรง | ถ้าไม่ตั้ง DATABASE_URL จะใช้ SQLite (`sqlite:///./dev.db`) ตามที่ plan ตั้งใจไว้สำหรับ Codespace |
| backend/app/db/migrations/001_init.py: upgrade | CON-TECH-01, DOM-PDPA-01, IF-HIS-01 | ตรง | |
| backend/app/main.py: app, lifespan | ไม่มี (T-02, T-03) | ตรง | รวม router เท่านั้น |
| frontend/src/api/client.js: getSlots, createBooking | plan ข้อ 4 | ตรงบางส่วน | createBooking ยังไม่ส่ง header Authorization ซึ่งจะถูกปฏิเสธตาม IF-IDP-01 แต่ T-12 (ต่อ API จริง) ยังไม่ได้ทำ จึงยังไม่นับเป็นข้อค้นพบ |
| frontend/src/App.jsx, main.jsx | ไม่มี | ตรง | โครงเริ่มต้นของรายวิชา |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
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

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| (ยังไม่มี) | rtm.md นี้สร้างครั้งแรก บั๊ก `slot.remaining < 0` ใน service.py ถูกแก้เป็น `<= 0` ตามที่ทีมสั่งก่อน /verify ครั้งนี้ จึงไม่มี F-ID | test_TC_BKG_01_3_no_seat_left ไม่ผ่านกับโค้ดเดิม (`assert 1 == 0`) และผ่านกับโค้ดที่แก้แล้ว (บันทึกใน prompt-log.md 2569-10-07) |
