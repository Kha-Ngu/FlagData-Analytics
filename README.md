# UN FlagData Analytics  
A Python-based exploratory data analysis project using the UCI Flags Dataset to uncover patterns in national attributes such as language, landmass, population, and symbolic features of country flags.

---

## 📌 Overview  
**Author:** Khanh Nguyen  
**Language:** Python  
**Tools Used:** Pandas  
**Dataset Source:** UCI Machine Learning Repository (Flags Dataset)  
**Sample Size:** 194 countries  
**Features:** 30 flag-related attributes

---

## 🧠 Objective  
To analyze global distributions of countries by region and language, investigate how symbolic flag elements relate to demographics, and demonstrate data aggregation and merging techniques using real-world geopolitical data.

---

## 🌍 Key Variables  
- **Geographical:** Landmass, Zone, Area  
- **Demographic:** Population, Language  
- **Symbolic:** Colors (Red, Blue, Green, etc.), Stripes, Bars, Crosses, Crescents, Icons, Text  
- **Categorical:** Main flag color, Religion, Continent

---

## 🛠 Project Tasks & Code Flow  

### ✅ Task 1: Load and Label Data  
- Reads the raw `flag.data` file (without headers)  
- Assigns descriptive column names to improve readability  

### ✅ Task 2: Regional Filtering  
- Counts the number of countries located in North America (landmass code `1`)

### ✅ Task 3: Frequency Analysis  
- Uses both explicit loops and Pandas’ `value_counts()` to compute the number of countries per landmass  
- Demonstrates the efficiency of vectorized operations in data analysis  

### ✅ Task 4: Population by Language  
- Aggregates total population by official language  
- Recalculates for countries with populations under 50 million  
- Key takeaway: Smaller countries tend to speak less globally dominant languages

### ✅ Task 5: Language Merge Simulation  
- Creates a mock sales-rep dataset where each rep speaks a language  
- Merges with the flag dataset on the `language` field  
- Calculates total number of “representative countries” (with some double-counting for shared languages)

### ✅ Task 6: Pivot Table of Area  
- Builds a pivot table showing the total land area for each `(landmass, language)` combination  
- Interprets missing combinations as NaN values, indicating language gaps in regions

---

## 📈 Sample Output  
```plaintext
*** Task 2 ***
Number of countries in North America: 23

*** Task 4 ***
Language 6: 3.45 billion population
Language 7: 1.38 billion population
...
Language 10: Most common in small-population countries
🔍 Insights & Interpretations
Language 6 (Indo-European) is the most widely spoken group by total population

Language 10 (Others) appears frequently among smaller, less-populous countries

Some landmass-language combinations have no representation, resulting in NaN values in the pivot```
```
## 📎 File Structure
<pre><code>
project-root/
├── flag.data                 # Raw dataset (no header)
├── FlagData Analytics.py     # Python script with 6 analysis tasks
└── README.md                 # Project documentation               
</code></pre>

## 🔍 Insights & Interpretations
- Language 6 (Indo-European) is the most widely spoken group by total population
- Language 10 (Others) appears frequently among smaller, less-populous countries
- Some landmass-language combinations have no representation, resulting in NaN values in the pivot
---

## 📚 Conclusion

**FlagData Analytics** demonstrates how symbolic elements, languages, and geographic attributes can be explored through structured data analysis. The project emphasizes:

- ✅ Clarity in data loading and labeling
- ✅ Modular, task-based scripting
- ✅ Real-world application of Pandas operations
- ✅ Interpretability of aggregated metrics and pivots
