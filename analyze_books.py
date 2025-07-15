import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('all_books.csv')

print(df.head())

rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}
df['Rating_Num'] = df['Rating'].map(rating_map)

print(f"\nTotal books: {len(df)}")

print(f"Average book price: £{df['Price (£)'].mean():.2f}")

print("\nCheapest Book:")
print(df.loc[df['Price (£)'].idxmin()])

print("\nMost Expensive Book:")
print(df.loc[df['Price (£)'].idxmax()])

print("\nBooks per Rating:")
print(df['Rating'].value_counts())

print("\nAvailability:")
print(df['Availability'].value_counts())

sns.set(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Rating', hue='Rating', order=['One', 'Two', 'Three', 'Four', 'Five'], palette='viridis')
plt.title('Number of Books per Rating')
plt.xlabel('Rating')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()

availability_counts = df['Availability'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(availability_counts, labels=availability_counts.index, autopct='%1.1f%%', colors=['#a1c9f4','#ffb482'])
plt.title('Book Availability')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['Price (£)'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Book Prices')
plt.xlabel('Price(£)')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()



