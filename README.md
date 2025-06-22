

# 🗳️ Simple Voting System in Python

This is a **console-based voting system** implemented in Python. The application allows users to:

* Add candidates
* Display the list of candidates
* Vote for a candidate
* View election results

---

## 📁 Project Structure

```plaintext
voting_system.py  # Main Python script containing the implementation
```

---

## ▶️ How to Run

### Requirements

* Python 3.x installed

### Steps

1. **Clone or download** this repository.
2. Open a terminal and navigate to the folder.
3. Run the program:

   ```bash
   python voting_system.py
   ```

---

## 🧠 How It Works

1. **Candidates are added** during the initial setup inside the `main()` function.
2. **Menu options** allow the user to:

   * View available candidates
   * Vote by entering the candidate number
   * See live election results
   * Exit the system

---

## 📌 Sample Output

```plaintext
Options:
1. Display Candidates
2. Vote
3. Display Results
4. Exit
Select an option: 1
Candidates:
1. Candidate A
2. Candidate B

Select an option: 2
Enter the number of the candidate you want to vote for: 1
You've voted for Candidate A!

Select an option: 3
Election Results:
Candidate A: 1 votes
Candidate B: 0 votes
```

---

## ✅ Features

* Simple CLI interface
* Error handling for invalid input
* Persistent vote count during the session

---

## 🚀 Future Improvements

* Save votes to a file or database
* Prevent duplicate voting
* Add authentication or user registration
* Graphical User Interface (GUI)

---

## 📄 License

This project is open source and free to use for educational purposes.
