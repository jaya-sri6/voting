class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

class VotingSystem:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def display_candidates(self):
        print("Candidates:")
        for i, candidate in enumerate(self.candidates):
            print(f"{i + 1}. {candidate.name}")

    def vote(self, candidate_index):
        if 1 <= candidate_index <= len(self.candidates):
            candidate = self.candidates[candidate_index - 1]
            candidate.votes += 1
            print(f"You've voted for {candidate.name}!")
        else:
            print("Invalid candidate selection.")

    def display_results(self):
        print("Election Results:")
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")

def main():
    voting_system = VotingSystem()

    # Add candidates
    candidate1 = Candidate("Candidate A")
    candidate2 = Candidate("Candidate B")
    voting_system.add_candidate(candidate1)
    voting_system.add_candidate(candidate2)

    while True:
        print("\nOptions:")
        print("1. Display Candidates")
        print("2. Vote")
        print("3. Display Results")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            voting_system.display_candidates()
        elif choice == "2":
            voting_system.display_candidates()
            try:
                candidate_index = int(input("Enter the number of the candidate you want to vote for: "))
                voting_system.vote(candidate_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            voting_system.display_results()
        elif choice == "4":
            print("Exiting the voting system.")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
