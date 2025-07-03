# 🤖 AI Agent – Predict, Explain & Advise

## 📌 Περιγραφή

Αυτό το πρόγραμμα είναι ένας **AI Agent** που χρησιμοποιεί ένα ήδη εκπαιδευμένο μοντέλο μηχανικής μάθησης (Random Forest) για να:

- Κάνει πρόβλεψη του επιπέδου εθισμού ενός φοιτητή στα social media.
- Παρέχει εξηγήσεις σε φυσική γλώσσα για τη λογική της πρόβλεψης.
- Δίνει εξατομικευμένες συμβουλές για βελτίωση.
- Περιλαμβάνει μια προαιρετική **what-if ανάλυση** με βάση καλύτερο ύπνο.

## 👤 Ονοματεπώνυμο & ΑΜ

**Ονοματεπώνυμο:** Γιώργος Κουτσούδης  
**Αριθμός Μητρώου (ΑΜ):** 12345678

## 🎯 Τι κάνει ο Agent

Ο Agent:

- Ζητά από τον χρήστη (μέσω τερματικού) να απαντήσει σε 4 ερωτήσεις:
  - Χρήση social media (ώρες)
  - Ύπνος (ώρες)
  - Επιρροή στην ακαδημαϊκή απόδοση
  - Καυγάδες λόγω social media
- Κάνει πρόβλεψη επιπέδου εθισμού: `Low`, `Medium` ή `High`
- Παρέχει αναφορά με:
  - 📍 Εξηγήσεις (explanations)
  - 💡 Συμβουλές (advice)
  - 🔄 What-if analysis (αν κοιμόταν 8 ώρες)

## 💬 Παράδειγμα Απόκρισης

> **Predicted Addiction Level:** High  
> **Explanation:**
> - Your daily social media usage is high.
> - Your sleep duration is lower than the recommended amount.  
> **Suggestions:**
> - Try to reduce your daily social media usage.
> - Prioritize sleep — aim for at least 7–8 hours.  
> **What-if Analysis:** If you slept 8 hours, the prediction would change to: **Medium**

## ▶️ Οδηγίες Εκτέλεσης

1. **Προαπαιτούμενο:**  
   Ο Agent χρειάζεται ένα εκπαιδευμένο μοντέλο τύπου `RandomForestClassifier`, το οποίο έχει φορτωθεί και είναι διαθέσιμο ως μεταβλητή `model`.

2. **Εκτέλεση:**  
   Αν το αρχείο αποθηκευτεί ως `ai_agent_social_addiction.py`, εκτελέστε:

   ```bash
   python ai_agent_social_addiction.py
