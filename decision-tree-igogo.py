decision_tree = {
    "Is it fiction?": {
        "Yes": {
            "Is it a mystery?": {
                "Yes": "Mystery",
                "No": "General Fiction"
            }
        },
        "No": {
            "Is it a biography?": {
                "Yes": "Biography",
                "No": "Non-Fiction"
            }
        }
    }
}


def classify_book(decision_tree):
    # Start at the root of the decision tree
    node = decision_tree

    # Loop through the questions until we reach a genre
    while isinstance(node, dict):
        question = list(node.keys())[0]
        answer = input(question + " ")
        node = node[answer]

    # Print the final genre
    print("Genre:", node)

classify_book(decision_tree)
