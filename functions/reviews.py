def add_review(reviews: list) -> list:
    review = input("Залиште свій відгук\n->")
    reviews.append(review)
    print("Ваш відгук успішно збережено.")
    return reviews


def find_dublicate_char(reviews: list[str]) -> None:
    reviews = " ".join(reviews).lower()

    repeated_groups = set()
    for i in range(len(reviews)):
        for j in range(i+1, len(reviews)):
            if reviews.count(reviews[i:j]) >= 2:
                repeated_groups.add(reviews[i:j])

    print(f"Групи символів, які повторюються не менше двох разів у відгуках:\n{repeated_groups}\n")
    