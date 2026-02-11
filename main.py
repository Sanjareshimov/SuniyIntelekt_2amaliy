import pandas as pd
import numpy as np

# 1. CSV faylni yuklash
df = pd.read_csv("10.csv")

print("📌 Jadval ustunlari:")
print(df.columns)

# 2. Takroriy qatorlarni olib tashlash (console uchun)
clean_df = df.drop_duplicates()

print("\n📌 Takroriy qatorlar olib tashlangandan keyingi ma'lumotlar:")
print(clean_df)

# 3. GroupBy (masalan Level bo‘yicha)
grouped = clean_df.groupby("Level")

# 4. Sonli ustunlarning o‘rtacha qiymatlari
mean_values = grouped[["Weight", "Amount"]].mean()

print("\n📊 GroupBy(Level) bo‘yicha o‘rtacha qiymatlar:")
print(mean_values)

# 5. Tozalangan ma’lumotni yangi CSV faylga saqlash
clean_df.to_csv("10_cleaned.csv", index=False)

print("\n✅ Tozalangan fayl '10_cleaned.csv' nomi bilan saqlandi")
