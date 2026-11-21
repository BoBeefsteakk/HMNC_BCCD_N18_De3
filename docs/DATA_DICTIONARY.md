# Từ điển dữ liệu (Data Dictionary) — Đề 3: Dự báo phụ tải điện Panama

> **Thuộc nhiệm vụ:** Task T004 (Đỗ Minh Huấn), kiểm tra theo tiêu chí chấm **B1.2** (0,25 điểm).  
> **Ánh xạ báo cáo:** Bảng 1.1 trong Báo cáo chuyên đề (ghi vết tại `docs/trace_huan.md`).  
> **Nguồn dữ liệu gốc:** Mendeley Data, doi:10.17632/byx7sztj59.1 (CC BY 4.0), tác giả: Carlos A. Pachon et al.  
> **Bộ tệp khảo sát:** `continuous.csv` (48.048 dòng, 17 cột) và `forecast_cnd.csv` (40.152 dòng, 2 cột) trong `data/raw/`.

---

## 1. Bảng từ điển dữ liệu tổng thể (`continuous.csv`)

Bảng dưới đây mô tả chi tiết toàn bộ 17 trường thông tin có trong tệp dữ liệu chính `data/raw/continuous.csv`, đáp ứng đầy đủ 5 tiêu chí: **Tên cột, Ý nghĩa nghiệp vụ/vật lý, Đơn vị đo, Kiểu dữ liệu, Thang đo**, cùng cột **Nguồn trích dẫn**.

| STT | Tên cột | Ý nghĩa nghiệp vụ & vật lý | Đơn vị | Kiểu dữ liệu | Thang đo | Nguồn trích dẫn |
|---|---|---|---|---|---|---|
| 1 | `datetime` | Mốc thời gian ghi nhận dữ liệu theo giờ tại Panama (Múi giờ UTC-05:00). Dữ liệu gốc ghi nhãn là thời điểm kết thúc giờ (end-of-hour), sau tiền xử lý lùi 1 giờ (`TIMESTAMP_SHIFT_HOURS = -1`) để đưa về mốc đầu giờ. | Thời gian ISO-8601 (`YYYY-MM-DD HH:MM:SS`) | `object` / `datetime64[ns]` | Khoảng (Interval) | `columns_metadata.pdf` (tr. 1); `CONVENTIONS.md` (mục 1) |
| 2 | `nat_demand` | **Biến mục tiêu (Target)**: Tổng nhu cầu phụ tải điện toàn quốc của Panama trong 1 giờ. | MWh (Megawatt-giờ) | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1); `src/config.py` (`TARGET_COL`) |
| 3 | `T2M_toc` | Nhiệt độ không khí ở độ cao 2 mét tại trạm Tocumen (vùng thủ đô Panama City, nơi tiêu thụ điện lớn nhất). | °C | `float64` | Khoảng (Interval) | `columns_metadata.pdf` (tr. 1) |
| 4 | `QV2M_toc` | Độ ẩm tại trạm Tocumen theo mô tả tác giả (*Relative humidity*, PDF tr. 1). *Ghi chú [Suy luận nhóm từ dải giá trị thực nghiệm]: Dải số thực tế là 0,012 – 0,023, phù hợp với thang đo tỷ ẩm riêng (Specific humidity, kg/kg).* | % (mô tả PDF); dải số thực nghiệm 0,012–0,023 | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1); quan sát dữ liệu thực tế |
| 5 | `TQL_toc` | Lượng mưa lỏng (Liquid precipitation) tại trạm Tocumen theo mô tả tài liệu gốc. | l/m² (tương đương mm) | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1) |
| 6 | `W2M_toc` | Tốc độ gió ở độ cao 2 mét (Wind Speed at 2 meters) tại trạm Tocumen. | m/s | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1) |
| 7 | `T2M_san` | Nhiệt độ không khí ở độ cao 2 mét tại trạm Santiago (miền trung Panama, thủ phủ tỉnh Veraguas). | °C | `float64` | Khoảng (Interval) | `columns_metadata.pdf` (tr. 1) |
| 8 | `QV2M_san` | Độ ẩm tại trạm Santiago theo mô tả tác giả. *Ghi chú [Suy luận nhóm từ dải giá trị thực nghiệm]: Dải số thực tế là 0,010 – 0,022, phù hợp với tỷ ẩm riêng (kg/kg).* | % (mô tả PDF); dải số thực nghiệm 0,010–0,022 | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1); quan sát dữ liệu thực tế |
| 9 | `TQL_san` | Lượng mưa lỏng tại trạm Santiago theo mô tả tài liệu gốc. | l/m² | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1) |
| 10 | `W2M_san` | Tốc độ gió ở độ cao 2 mét tại trạm Santiago. | m/s | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1) |
| 11 | `T2M_dav` | Nhiệt độ không khí ở độ cao 2 mét tại trạm David (miền tây Panama, thủ phủ tỉnh Chiriquí, trung tâm nông nghiệp/thương mại lớn). | °C | `float64` | Khoảng (Interval) | `columns_metadata.pdf` (tr. 1) |
| 12 | `QV2M_dav` | Độ ẩm tại trạm David theo mô tả tác giả. *Ghi chú [Suy luận nhóm từ dải giá trị thực nghiệm]: Dải số thực tế là 0,010 – 0,021, phù hợp với tỷ ẩm riêng (kg/kg).* | % (mô tả PDF); dải số thực nghiệm 0,010–0,021 | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1); quan sát dữ liệu thực tế |
| 13 | `TQL_dav` | Lượng mưa lỏng tại trạm David theo mô tả tài liệu gốc. | l/m² | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1) |
| 14 | `W2M_dav` | Tốc độ gió ở độ cao 2 mét tại trạm David. | m/s | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1) |
| 15 | `Holiday_ID` | Mã định danh duy nhất cho ngày lễ: giá trị 0 là ngày thường, các giá trị 1 đến 22 tương ứng với 22 ngày lễ cụ thể trong năm tại Panama (xem Bảng tra cứu Mục 2). | Mã số nguyên danh mục | `int64` | Định danh (Nominal) | `columns_metadata.pdf` (tr. 1 & tr. 2) |
| 16 | `holiday` | Cờ nhị phân chỉ thị ngày nghỉ lễ: 1 = ngày nghỉ lễ, 0 = ngày làm việc bình thường. | Nhị phân {0, 1} | `int64` | Định danh nhị phân (Nominal/Binary) | `columns_metadata.pdf` (tr. 1) |
| 17 | `school` | Cờ nhị phân chỉ thị kỳ đi học của học sinh/sinh viên: 1 = trong kỳ học, 0 = kỳ nghỉ học / nghỉ hè. | Nhị phân {0, 1} | `int64` | Định danh nhị phân (Nominal/Binary) | `columns_metadata.pdf` (tr. 1) |

---

## 2. Bảng tra cứu danh mục ngày lễ (`Holiday_ID`)

Được trích xuất từ tài liệu đi kèm của bộ dữ liệu (`data/raw/columns_metadata.pdf`, trang 2):

| Mã `Holiday_ID` | Tên ngày lễ (Tiếng Anh) | Tên ngày lễ (Dịch nghĩa tiếng Việt) |
|---|---|---|
| **0** | Regular day | Ngày làm việc bình thường |
| **1** | New Year | Tết Dương lịch (01/01) |
| **2** | Martyrs' Day | Ngày các Liệt sĩ (09/01) |
| **3** | Carnival Saturday | Thứ Bảy Lễ hội Carnival |
| **4** | Carnival Sunday | Chủ Nhật Lễ hội Carnival |
| **5** | Carnival Monday | Thứ Hai Lễ hội Carnival |
| **6** | Carnival Tuesday | Thứ Ba Lễ hội Carnival |
| **7** | Ash Wednesday | Thứ Tư Lễ Tro |
| **8** | Holy Thursday | Thứ Năm Tuần Thánh |
| **9** | Good Friday | Thứ Sáu Tuần Thánh |
| **10** | Holy Saturday | Thứ Bảy Tuần Thánh |
| **11** | Resurrection Sunday | Chủ Nhật Phục Sinh |
| **12** | Labor Day | Ngày Quốc tế Lao động (01/05) |
| **13** | Foundation of Old Panama | Ngày thành lập thành phố cổ Panama (15/08) |
| **14** | Separation of Panama from Colombia | Ngày Panama tách khỏi Colombia (03/11) |
| **15** | Flag Day | Ngày Quốc kỳ Panama (04/11) |
| **16** | Patriotic Commemoration in Colón city | Ngày Kỷ niệm Ái quốc tại thành phố Colón (05/11) |
| **17** | First Cry of Independence | Tiếng chuông Độc lập đầu tiên tại La Villa de Los Santos (10/11) |
| **18** | Independence of Panama from Spain | Ngày Độc lập khỏi Tây Ban Nha (28/11) |
| **19** | Mother's Day | Ngày của Mẹ (08/12) |
| **20** | Christmas eve | Đêm Giáng sinh (24/12) |
| **21** | Christmas | Ngày Lễ Giáng sinh (25/12) |
| **22** | New Year's Eve | Đêm Giao thừa (31/12) |

---

## 3. Từ điển dữ liệu tệp dự báo điều độ tuần của CND (`forecast_cnd.csv`)

Tệp `data/raw/forecast_cnd.csv` lưu trữ kết quả dự báo phụ tải trước vận hành tuần (weekly pre-dispatch forecast) chính thức của Trung tâm Điều độ Quốc gia Panama (CND - *Centro Nacional de Despacho*), dùng làm mô hình đối chứng cơ sở (baseline benchmark).

| Tên cột | Ý nghĩa nghiệp vụ | Đơn vị | Kiểu dữ liệu | Thang đo | Nguồn trích dẫn |
|---|---|---|---|---|---|
| `datetime` | Mốc thời gian dự báo của báo cáo CND. Định dạng chuỗi ban đầu `M/D/YYYY H:MM`. Khi căn chỉnh phụ tải thực tế áp dụng dịch `-1` giờ (`CND_SHIFT_HOURS = -1`) do nhãn gốc CND đồng pha với giờ kết thúc của phụ tải. | Thời gian | `object` / `datetime64[ns]` | Khoảng (Interval) | `columns_metadata.pdf` (tr. 1); `src/config.py` |
| `load_forecast` | Dự báo phụ tải điện theo giờ do chuyên gia CND công bố trước tuần vận hành. | MWh | `float64` | Tỷ lệ (Ratio) | `columns_metadata.pdf` (tr. 1); `forecast_cnd.csv` |

---

## 4. Thống kê mô tả định lượng (Quan sát thực nghiệm)

Thống kê tính toán trực tiếp trên toàn bộ 48.048 quan trắc giờ (từ 03/01/2015 01:00 đến 27/06/2020 00:00) của tệp `continuous.csv` và 40.152 giờ của tệp `forecast_cnd.csv`:

| Tên biến | Số lượng mẫu | Số giá trị thiếu (Null) | Giá trị nhỏ nhất (Min) | Giá trị trung bình (Mean) | Độ lệch chuẩn (Std) | Giá trị lớn nhất (Max) |
|---|---|---|---|---|---|---|
| `nat_demand` | 48.048 | 0 (0,0%) | 85,1925 | 1.182,8686 | 192,0689 | 1.754,8820 |
| `T2M_toc` | 48.048 | 0 (0,0%) | 22,9535 | 27,3991 | 1,6755 | 35,0396 |
| `QV2M_toc` | 48.048 | 0 (0,0%) | 0,0121 | 0,0183 | 0,0016 | 0,0227 |
| `TQL_toc` | 48.048 | 0 (0,0%) | 0,0000 | 0,0800 | 0,0656 | 0,5212 |
| `W2M_toc` | 48.048 | 0 (0,0%) | 0,0090 | 13,3910 | 7,2955 | 39,2297 |
| `T2M_san` | 48.048 | 0 (0,0%) | 19,7652 | 26,9210 | 3,0181 | 39,0634 |
| `QV2M_san` | 48.048 | 0 (0,0%) | 0,0102 | 0,0178 | 0,0019 | 0,0222 |
| `TQL_san` | 48.048 | 0 (0,0%) | 0,0000 | 0,1063 | 0,0863 | 0,4850 |
| `W2M_san` | 48.048 | 0 (0,0%) | 0,0604 | 7,0467 | 4,1037 | 24,4839 |
| `T2M_dav` | 48.048 | 0 (0,0%) | 19,9337 | 24,7195 | 2,4140 | 34,2162 |
| `QV2M_dav` | 48.048 | 0 (0,0%) | 0,0097 | 0,0169 | 0,0016 | 0,0211 |
| `TQL_dav` | 48.048 | 0 (0,0%) | 0,0000 | 0,1447 | 0,0879 | 0,4778 |
| `W2M_dav` | 48.048 | 0 (0,0%) | 0,0155 | 3,5676 | 1,7105 | 10,2889 |
| `Holiday_ID` | 48.048 | 0 (0,0%) | 0 | 0,7048 | 3,1475 | 22 |
| `holiday` | 48.048 | 0 (0,0%) | 0 | 0,0629 (6,29%) | 0,2429 | 1 |
| `school` | 48.048 | 0 (0,0%) | 0 | 0,7278 (72,78%) | 0,4451 | 1 |
| `load_forecast` (CND) | 40.152 | 0 (0,0%) | 0,0000 | 1.207,9293 | 195,2406 | 1.760,4000 |

---

## 5. Phát hiện và ghi chú quan trọng từ khảo sát dữ liệu

1. **Chất lượng dữ liệu ban đầu:** Bộ dữ liệu `continuous.csv` hoàn chỉnh, không có giá trị khuyết thiếu (`NaN = 0`), đúng 48.048 dòng giờ liên tục tương ứng với 286 tuần trọn vẹn ($\times 168$ giờ/tuần).
2. **Ký hiệu và dải giá trị biến độ ẩm `QV2M` [Suy luận nhóm từ dải giá trị thực nghiệm]:**
   - Trong tài liệu gốc (`columns_metadata.pdf` tr. 1), tác giả mô tả là *"Relative humidity (%)"*.
   - Tuy nhiên, quan sát dải số thực tế của `QV2M` trong dữ liệu chỉ dao động từ `0,010` đến `0,023` (trung bình `0,018`).
   - Nhóm đưa ra suy luận: dải số này phù hợp với thang đo *Specific Humidity* (tỷ ẩm riêng biệt, khối lượng hơi nước trên khối lượng không khí khô, kg/kg) thường gặp trong khí quyển, thay vì tỷ lệ phần trăm (0–100%) của độ ẩm tương đối.
   - Nhóm giữ nguyên tên cột và quy chuẩn theo `src/config.py`, chỉ lưu ý điểm khác biệt này để phục vụ chuẩn hóa đặc trưng chính xác.
3. **Khảo sát 72 giờ có giá trị bằng 0 trong tệp dự báo CND (`forecast_cnd.csv`):**
   - Qua rà soát chi tiết, 72 giờ ghi nhận `load_forecast = 0.0 MWh` **không phải là 1 khối duy nhất 3 ngày**, mà chia thành **2 đoạn liên tiếp riêng biệt trong năm 2016**:
     - *Đoạn 1:* **24 giờ liên tiếp**, từ dòng 1008 (`2/13/2016 0:00`) đến dòng 1031 (`2/13/2016 23:00`) — Thứ Bảy 13/02/2016.
     - *Đoạn 2:* **48 giờ liên tiếp**, từ dòng 7728 (`11/19/2016 0:00`) đến dòng 7775 (`11/20/2016 23:00`) — Thứ Bảy 19/11/2016 đến Chủ Nhật 20/11/2016.
   - **Vị trí tập dữ liệu:** Cả hai đoạn (tổng 72 giờ) đều nằm hoàn toàn trong **tập huấn luyện (train)** (năm 2015–2018).
   - **Ảnh hưởng đến MAPE ở bài toán R2:** Trong tập kiểm định (`val`: 26 tuần năm 2019) và tập kiểm tra (`test_a`: 37 tuần, `test_b`: 14 tuần), **số lượng giờ có phụ tải CND bằng 0 là 0 giờ**. Do đó, hiện tượng này **hoàn toàn không ảnh hưởng đến chỉ số MAPE của CND trong bài toán so sánh R2** (vì R2 chỉ đánh giá trên tập val và test).
4. **Các giờ phụ tải thấp bất thường trong `nat_demand`:**
   - Trong toàn bộ 48.048 giờ, có đúng 8 giờ ghi nhận phụ tải thấp bất thường (< 50% trung vị tập train = 1.156,71 MWh):
     - *Trong tập train (3 giờ):* 24/01/2015 16:00 (509,84 MWh; 44%), 27/06/2017 11:00 (380,59 MWh; 33%), 01/07/2017 13:00 (560,70 MWh; 48%).
     - *Trong tập val (5 giờ liên tiếp):* ngày 20/01/2019 từ 11:00 đến 15:00 (phụ tải giảm sâu xuống 85,19 – 475,80 MWh; từ 7% đến 41% mức bình thường).
     - *Trong tập test (test_a, test_b):* **0 giờ**.
   - **Nguyên nhân sự kiện:** `UNKNOWN` (chưa có tài liệu nguồn xác nhận nguyên nhân cụ thể, không đưa ra suy đoán cảm tính).
   - **Hướng xử lý (theo CONVENTIONS.md mục 8):** Giữ nguyên dữ liệu gốc; khi đánh giá mô hình trên tập val, nhóm sẽ báo cáo MAPE song song theo hai kịch bản: (1) toàn bộ tập val, và (2) tập val loại trừ 5 giờ bất thường ngày 20/01/2019 (do MAPE rất nhạy cảm khi mẫu số nhỏ đột biến).
