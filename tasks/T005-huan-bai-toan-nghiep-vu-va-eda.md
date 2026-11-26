---
id: T005
title: Bài toán nghiệp vụ và EDA
phase: P2
checklist: B1.1,B1.3
owner: huan
status: review
due: 26/11/2026
files: notebooks/huan_eda.ipynb,results/figures,docs/trace_huan.md
depends: T001
---
# T005 — Bài toán nghiệp vụ và EDA

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Phát biểu bài toán nghiệp vụ (ai dùng, quyết định gì, chi phí sai), chọn chỉ số chính MAPE và nêu lý do, làm EDA ≥ 4 hình mỗi hình ≥ 1 nhận xét định lượng, phát hiện ≥ 1 vấn đề dữ liệu và cách xử lý.


## Đầu vào cần đọc
- `TEAM.md`, `docs/CONVENTIONS.md`
- `docs/DE3.md` (B1.1, B1.3), `docs/CONVENTIONS.md` mục 4, 5
- `src/data_prep.py` sau khi T001 merge; `docs/DATA_DICTIONARY.md` (T004)
- `docs/HUAN.md`


## Không được làm
- AI được viết mã phần tự cài đặt (GD/SGD/mini-batch/momentum, PLA/Pocket, MLP + backprop, PCA, LDA), nhưng bạn phải giải thích được từng dòng và ghi `docs/ai_usage_log.md`.
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- `notebooks/huan_eda.ipynb` chạy từ đầu đến cuối, chỉ gọi hàm trong `src/`, đã XÓA output trước khi commit.
- ≥ 4 hình đặt tên `results/figures/1_<số>_*.png`, có tên trục và đơn vị, mỗi hình ≥ 1 nhận xét có con số.
- ≥ 1 vấn đề dữ liệu được nêu cùng cách xử lý.
- Mỗi hình có một dòng trong `docs/trace_huan.md`.
- `python -m pytest` không có test đỏ.


## Tôi giải thích được
- [x] Tôi tự giải thích được từng dòng mã và từng con số trong task này (người làm tự tick).

## Kết quả (người làm điền)
- **Tóm tắt khung bài toán nghiệp vụ (B1.1 — ghi chú ý chính, phần văn xuôi Huấn tự viết trên Google Docs):**
  - *Ai dùng & quyết định gì:* Trung tâm Điều độ Quốc gia Panama (CND) dùng dự báo phụ tải từng giờ cho tuần tới (168 giờ, Thứ Bảy 00:00 → Thứ Sáu 23:00, chốt dữ liệu đến hết Thứ Ba trước đó theo quy tắc khoảng trống 72 giờ) để lập kế hoạch huy động nguồn (weekly pre-dispatch) với chi phí thấp nhất và bảo đảm an ninh hệ thống [7].
  - *Chi phí từng loại sai (ví dụ định lượng từ `train`, không bịa đơn giá điện):* Dự báo **thấp hơn thực tế** gây thiếu nguồn dự phòng, phải huy động tổ máy dự phòng đắt hơn hoặc tăng rủi ro mất ổn định/sa thải phụ tải; dự báo **cao hơn thực tế** gây huy động thừa nguồn phát, lãng phí chi phí khởi động và nhiên liệu. Cụ thể trên tập huấn luyện, sai số **1%** tại mức phụ tải trung bình (`1.169,28 MWh`) tương ứng lệch **11,69 MWh**, còn tại giờ đỉnh lớn nhất của `train` (`1.645,48 MWh`) tương ứng lệch **16,45 MWh** trong một giờ.
  - *Biến mục tiêu & chỉ số đánh giá:* Biến mục tiêu hồi quy `nat_demand` (MWh). Chỉ số chính là **MAPE theo giờ của từng tuần kiểm tra rồi lấy trung bình các tuần** (báo cáo riêng giai đoạn (a) 37 tuần và (b) 14 tuần), phù hợp để so sánh trực tiếp theo đơn vị phần trăm với dự báo chính thức của CND và mô hình cơ sở (trễ 336 giờ; trung bình cùng giờ tuần 2, 3, 4 trước). Hạn chế của MAPE là rất nhạy với giờ phụ tải thấp bất thường nên đi kèm MAE, RMSE (MWh), sai số đỉnh/đáy/năng lượng tuần và chỉ số kỹ năng. Với bài toán phụ "giờ cao điểm" (phân lớp lệch lớp 10% dương / 90% âm trên `train`), không dùng accuracy đơn thuần mà dùng số lỗi theo epoch và các chỉ số phân lớp phù hợp ở Chương 4.
- **Notebook và tệp kết quả EDA (B1.3 — không đọc tập kiểm tra `test_a`, `test_b`):**
  - Đã tạo `notebooks/huan_eda.ipynb` (gọi trực tiếp `src/config.py` và `src/data_prep.py`, chỉ sử dụng `splits["train"]` và `splits["val"]`, chạy thông suốt từ Ô 1 → Ô 8 và đã xóa sạch toàn bộ output trước khi commit).
  - Đã xuất **Bảng 1.2** (`results/tables/1_2_eda_summary.csv`): thống kê mô tả của `nat_demand`, 12 biến thời tiết và 3 biến lịch trên `train` (35.112 giờ, `0` giá trị thiếu trên cả `train` và `val`).
  - Đã xuất **Bảng 1.3** (`results/tables/1_3_eda_breakdown.csv`): xuất toàn bộ số liệu phân tách dùng trong mục Kết quả (TB và cực đại theo năm 2015–2018 trên `train` và nửa đầu 2019 trên `val`; TB/ĐLC/đỉnh/đáy/biên độ/% thấp hơn theo loại ngày; tỷ lệ cao điểm `train` và `val`; thống kê 8 giờ tải thấp; độ dốc nhiệt độ và trung bình ngày làm việc theo dải `29–33 °C`; ví dụ sai số 1% cho B1.1).
  - Đã xuất **5 hình EDA** (đều có tên trục, đơn vị, chú giải) và ghi dòng truy vết đầy đủ (2 bảng + 5 hình) vào `docs/trace_huan.md`:
    1. **Hình 1.1** (`results/figures/1_1_load_timeseries_anomalies.png`): Phụ tải trung bình tăng đều qua từng năm: 2015 (`1.131,52 MWh`) → 2016 (`1.157,18 MWh`) → 2017 (`1.182,31 MWh`) → 2018 (`1.205,68 MWh`) → `val` nửa đầu 2019 (`1.248,11 MWh`, đỉnh `1.719,04 MWh`). Đánh dấu rõ 4 tuần khởi động đầu của `train` và **8 giờ tải thấp bất thường** (`< 50%` trung vị train = `578,36 MWh`).
    2. **Hình 1.2** (`results/figures/1_2_load_distribution_peak.png`): `nat_demand` trên `train` có trung bình `1.169,28 ± 191,75 MWh`, trung vị `1.156,71 MWh`, phân vị 90% = `1.450,75 MWh`. Áp dụng ngưỡng `1.450,75 MWh` của `train`, tỷ lệ nhãn giờ cao điểm `+1` tăng từ **10,00%** (3.512/35.112 giờ) trên `train` lên **17,54%** (766/4.368 giờ) trên `val` do xu hướng tăng phụ tải.
    3. **Hình 1.3** (`results/figures/1_3_diurnal_weekly_profile.png`): Chu kỳ ngày–đêm và theo loại ngày rất rõ trên `train`: ngày làm việc trung bình `1.214,73 ± 200,48 MWh` (đỉnh `12:00` đạt `1.475,36 MWh`, đáy `03:00` còn `931,95 MWh`, biên độ `543,41 MWh`); cuối tuần trung bình `1.084,16 ± 127,73 MWh` (thấp hơn ngày làm việc `10,75%`, đỉnh `10:00` đạt `1.207,53 MWh`); ngày lễ trung bình `1.039,76 ± 128,93 MWh` (thấp hơn `14,40%`, đỉnh dịch sang `18:00` đạt `1.156,38 MWh`).
    4. **Hình 1.4** (`results/figures/1_4_load_vs_temperature.png`): Nhiệt độ trung bình 3 thành phố `T2M_mean` trên `train` (21,06–35,37 °C, TB `26,27 °C`) tương quan dương mạnh với phụ tải ($r = 0{,}684$), độ dốc hồi quy tuyến tính tổng thể **+58,01 MWh/°C**; tách biệt rõ 2 nhánh ngày làm việc (ở dải `29–31 °C`, trung bình đạt `1.449,12 MWh` ở `(29, 30] °C` và `1.442,88 MWh` ở `(30, 31] °C` — vẫn dưới ngưỡng `1.450,75 MWh`, và **chỉ vượt ngưỡng cao điểm từ khoảng `> 31 °C`** với `1.463,99 MWh` ở dải `(31, 32] °C`) và cuối tuần/ngày lễ (đi ngang quanh `1.150–1.175 MWh`).
    5. **Hình 1.5** (`results/figures/1_5_correlation_heatmap.png`): Nhiệt độ 3 thành phố có tương quan cao nhất với `nat_demand` (`T2M_toc` $r = 0{,}69$, `T2M_dav` $r = 0{,}68$, `T2M_san` $r = 0{,}65$), trong khi `holiday` tương quan âm ($r = -0{,}17$). Đáng chú ý, tồn tại **đa cộng tuyến cực mạnh** giữa 3 thành phố: `T2M` đạt $r = 0{,}92\text{--}0{,}96$ (`T2M_san` vs `T2M_dav` = `0,96`), `QV2M` đạt $r = 0{,}82\text{--}0{,}92$.
- **Vấn đề dữ liệu phát hiện và cách xử lý:**
  1. **8 giờ phụ tải thấp bất thường (`< 50%` trung vị train = 578,36 MWh):** gồm 3 giờ đơn lẻ trong `train` (24/01/2015 16:00: `509,84 MWh`; 27/06/2017 11:00: `380,59 MWh`; 01/07/2017 13:00: `560,70 MWh`) và **5 giờ liên tiếp ngày 20/01/2019 (11:00–15:00) trong `val`** tụt xuống sâu nhất **85,19 MWh** (`7,4%` trung vị train). *Cách xử lý:* không xóa/nội suy làm sai lệch chuỗi thực, đánh dấu bằng `data_prep.low_load_hours()` và báo MAPE trên `val` cả khi có và không có 5 giờ ngày 20/01/2019, kèm MAE/RMSE.
  2. **Xu hướng tăng tải theo năm và dịch chuyển tỷ lệ nhãn cao điểm (10,00% → 17,54%):** chuỗi không dừng. *Cách xử lý:* chia dữ liệu theo thời gian tuần Thứ Bảy → Thứ Sáu (`209/26/37/14` tuần), không xáo trộn/không k-fold, mọi chuẩn hóa và ngưỡng chỉ khớp trên `train`, bỏ 4 tuần khởi động (`data_prep.drop_warmup`) khi huấn luyện, dùng đặc trưng trễ hợp lệ $\ge 240$ giờ.
  3. **Đa cộng tuyến cao giữa 12 biến thời tiết ($r = 0{,}92\text{--}0{,}96$ ở `T2M`) và hạn chế dữ liệu thời tiết tái phân tích:** lý giải số điều kiện lớn ở hồi quy tuyến tính (B3) và dẫn tới PCA/chọn đặc trưng (B6); nêu rõ hạn chế giả định dự báo thời tiết hoàn hảo trong báo cáo.
- **Kiểm thử:**
  - Chạy toàn bộ `notebooks/huan_eda.ipynb` từ đầu đến cuối: thành công, xuất đủ 2 bảng (`1_2`, `1_3`) và 5 hình; notebook đã xóa sạch output trước khi commit.
  - `python -m pytest`: **118 passed, 3 skipped, 0 failed**.
  - `python scripts/tasks.py check` và `python scripts/ai_log.py check`: 0 lỗi.
- Tự kiểm hiểu (model hỏi):
  - `notebooks/huan_eda.ipynb` (Ô 1–8) | qua | 26/11/2026 (3 câu: vì sao chỉ tính ngưỡng 90% và trung vị trên `train` không chạm `test_a`/`test_b` để tránh rò rỉ dữ liệu; vị trí 8 giờ tải thấp 3 `train` / 5 `val` ngày 20/01/2019 xuống `85,19 MWh`, vì sao làm vọt MAPE do $y_i$ ở mẫu số và cách xử lý giữ nguyên + báo MAPE 2 cách kèm MAE/RMSE; đa cộng tuyến `T2M` $r=0{,}92\text{--}0{,}96$ trên Hình 1.5 và mốc nhiệt độ vượt ngưỡng cao điểm `> 31 °C` trên Hình 1.4; sửa nhỏ: đổi `med_train` sang tính trên `train + val` → vi phạm rò rỉ dữ liệu và đẩy trung vị từ `1.156,71` lên `1.166,64 MWh`, tăng ngưỡng `low_thr` thêm `+4,96 MWh` lên `583,32 MWh`)

## Ghi chú AI đã dùng
Đã thêm 2 dòng vào `docs/ai_usage_log.md` (1 dòng loại M viết mã notebook và xuất 2 bảng/5 hình EDA; 1 dòng loại D hỏi kiểm hiểu 3 câu + sửa nhỏ và giải thích số liệu); phần văn xuôi Chương 1 (B1.1, B1.3) và báo cáo tiến độ T008 Huấn tự viết trên Google Docs.
