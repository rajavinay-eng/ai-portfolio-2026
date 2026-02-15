import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Load data

df = pd.read_csv("Swiss-salary-snapshot/data/data.csv")

print("Rows:", len(df))
print("\nFirst 5 rows:")
print(df.head())

# 2. NumPy statistics

salary_array = df["salary_chf"].to_numpy()

print("\nSalary statistics:")
print("Mean:", int(np.mean(salary_array)))
print("Median:", int(np.median(salary_array)))
print("Min:", int(np.min(salary_array)))
print("Max:", int(np.max(salary_array)))

# 3. Pandas analysis

city_avg = df.groupby("city")["salary_chf"].mean().sort_values(ascending=False)
print("\nAverage salary by city:")
print(city_avg)

# 4. Plot 1 — Average salary by city

plt.figure()
city_avg.plot(kind="bar")
plt.title("Average Salary by City (CHF)")
plt.xlabel("City")
plt.ylabel("Average Salary (CHF)")
plt.tight_layout()
plt.savefig("Swiss-salary-snapshot/outputs/avg_salary_by_city.png", dpi=200)
plt.show()


# 5. Plot 2 — Salary distribution

plt.figure()
plt.hist(df["salary_chf"], bins=8)
plt.title("Salary Distribution (CHF)")
plt.xlabel("Salary (CHF)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Swiss-salary-snapshot/outputs/salary_distribution.png", dpi=200)
plt.show()


# 6. Plot 3 — Salary vs experience

plt.figure()
plt.scatter(df["experience_years"], df["salary_chf"])
plt.title("Salary vs Experience")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (CHF)")
plt.tight_layout()
plt.savefig("Swiss-salary-snapshot/outputs/salary_vs_experience.png", dpi=200)
plt.show()


