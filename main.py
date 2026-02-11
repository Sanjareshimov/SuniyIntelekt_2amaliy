import pandas as pd
import numpy as np

# 1. CSV faylni yuklash
df = pd.read_csv("4.csv")

# 2. Jadval ustunlarini chiqarish
print("📌 Jadval ustunlari:")
print(df.columns)

# 3. Takroriy qatorlarni olib tashlash (faqat ishlash jarayonida)
clean_df = df.drop_duplicates()

print("\n📌 Tozalangan ma'lumotlar (takroriylar olib tashlandi):")
print(clean_df)

# 4. GroupBy (masalan Subject bo‘yicha)
grouped = clean_df.groupby("Subject")

# 5. Sonli ustun (Data_value) o‘rtacha qiymati
mean_values = grouped["Data_value"].mean()

print("\n📊 Subject bo‘yicha Data_value o‘rtacha qiymatlari:")
print(mean_values)

# 6. Tozalangan ma’lumotni yangi CSV faylga saqlash
clean_df.to_csv("file2_cleaned.csv", index=False)

print("\n✅ Tozalangan fayl 'file2_cleaned.csv' nomi bilan saqlandi")
