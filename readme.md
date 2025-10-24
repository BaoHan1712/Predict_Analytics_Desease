link dữ liệu: `https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset?utm_source=chatgpt.com`

Bộ dữ liệu này có từ năm 1988 và bao gồm bốn cơ sở dữ liệu: Cleveland, Hungary, Thụy Sĩ và Long Beach V. Nó chứa 76 thuộc tính, bao gồm cả thuộc tính dự đoán, nhưng tất cả các thí nghiệm đã công bố đều sử dụng một tập hợp con gồm 14 thuộc tính. Trường "mục tiêu" đề cập đến sự hiện diện của bệnh tim ở bệnh nhân. Nó có giá trị nguyên, 0 = không có bệnh và 1 = có bệnh.

| **Tên cột (Column Name)**              | **Mô tả (Description)**                          | **Kiểu dữ liệu / Giá trị (Type / Values)**                                                             |
| -------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `age`                                  | Tuổi của bệnh nhân                               | Số (integer)                                                                                           |
| `sex`                                  | Giới tính của bệnh nhân                          | 1 = Nam, 0 = Nữ                                                                                        |
| `chest pain type`                      | Loại đau ngực mà bệnh nhân gặp phải              | 1 = Đau thắt ngực điển hình<br>2 = Không điển hình<br>3 = Đau không do tim<br>4 = Không có triệu chứng |
| `resting blood pressure`               | Huyết áp khi nghỉ ngơi                           | Số (numeric)                                                                                           |
| `serum cholestoral in mg/dl`           | Nồng độ cholesterol trong huyết thanh            | Số (numeric)                                                                                           |
| `fasting blood sugar > 120 mg/dl`      | Đường huyết lúc đói > 120 mg/dl                  | 1 = Có, 0 = Không                                                                                      |
| `resting electrocardiographic results` | Kết quả điện tâm đồ khi nghỉ                     | 0 = Bình thường<br>1 = Bất thường ST-T<br>2 = Phì đại thất trái                                        |
| `maximum heart rate achieved`          | Nhịp tim tối đa đạt được khi gắng sức            | Số (numeric)                                                                                           |
| `exercise induced angina`              | Đau thắt ngực khi gắng sức                       | 1 = Có, 0 = Không                                                                                      |
| `oldpeak`                              | Mức độ chênh ST do gắng sức so với lúc nghỉ      | Số thực (float)                                                                                        |
| `slope`                                | Độ dốc của đoạn ST ở đỉnh gắng sức               | 0 = Dốc xuống<br>1 = Phẳng<br>2 = Dốc lên                                                              |
| `number of major vessels`              | Số mạch máu lớn được nhuộm bởi fluoroscopy (0–3) | Số (integer)                                                                                           |
| `thal`                                 | Kết quả xét nghiệm Thallium (Thalassemia test)   | 0 = Bình thường<br>1 = Khiếm khuyết cố định<br>2 = Khiếm khuyết hồi phục                               |
| `target`                  | Tình trạng mắc bệnh tim                          | 0 = Không mắc bệnh<br>1 = Có bệnh tim                                                                  |


Thử trên mô hình ML sau:

- XGBoost
- Random Forest
- Support Vector Machine (SVM)