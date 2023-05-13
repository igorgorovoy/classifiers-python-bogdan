decision_tree = {
    "Is it undefine?": {
        "Yes": {
            "Is it a devops?": {
                "Yes": "Devops",
                "No": "Python"
            }
        },
        "No": {
            "Is it a biography?": {
                "Yes": "Biography",
                "No": "Non-Fiction",
                "Documentation": {
                    "Does it have a format?": {
                    "URl": "Save as url in confluence",
                    "PDF": "Save as file in catalog",
                    "Directory": "Save as directory using rsync"
            }
        }
            }
        }
    },
        "Documentation": {
            "Does it have a format?": {
                "URl": "Save as url in confluence",
                "PDF": "Save as file in catalog",
                "Directory": "Save as directory using rsync"
            }
        }
}


def classify_book(decision_tree):
    # Start at the root of the decision tree
    node = decision_tree

    # Loop through the questions until we reach a genre
    while isinstance(node, dict):
        question = list(node.keys())[0]
        answer_options = list(node[question].keys())
        answer = input(f"{question} ({'/'.join(answer_options)}) ")

        # Check if answer is valid
        while answer not in answer_options:
            print(f"Invalid answer '{answer}'. Please choose from the following options: {', '.join(answer_options)}")
            answer = input(f"{question} ({'/'.join(answer_options)}) ")

        node = node[question][answer]

    # Print the final genre
    print("Genre:", node)


classify_book(decision_tree)
