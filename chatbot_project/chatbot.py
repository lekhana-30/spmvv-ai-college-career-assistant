import json
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.preprocessing import preprocess_text


class ChatBot:

    def __init__(self):

        self.questions = []
        self.answers = []

        # Get the folder where chatbot.py is located
        base_dir = os.path.dirname(
            os.path.abspath(__file__)
        )

        # Load SPMVV general FAQs
        self.load_faq_file(
            os.path.join(
                base_dir,
                "data",
                "spmvv_general.json"
            )
        )

        # Load B.Tech FAQs
        self.load_faq_file(
            os.path.join(
                base_dir,
                "data",
                "btech_faqs.json"
            )
        )

        # TF-IDF Vectorizer
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 3)
        )

        # Convert stored questions into vectors
        self.question_vectors = (
            self.vectorizer.fit_transform(
                self.questions
            )
        )

    # --------------------------------------------------
    # LOAD FAQ FILE
    # --------------------------------------------------

    def load_faq_file(self, filepath):

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        for faq in data["faqs"]:

            # Multiple question variations
            if "questions" in faq:

                for question in faq["questions"]:

                    processed_question = preprocess_text(
                        question
                    )

                    self.questions.append(
                        processed_question
                    )

                    self.answers.append(
                        faq["answer"]
                    )

            # Single question
            elif "question" in faq:

                processed_question = preprocess_text(
                    faq["question"]
                )

                self.questions.append(
                    processed_question
                )

                self.answers.append(
                    faq["answer"]
                )

    # --------------------------------------------------
    # GET RESPONSE
    # --------------------------------------------------

    def get_response(self, user_input):

        processed_input = preprocess_text(
            user_input
        )

        # Exact match first
        for i, question in enumerate(
            self.questions
        ):

            if processed_input == question:

                print("\n-------------------")
                print(
                    "User Input:",
                    user_input
                )
                print(
                    "Processed Input:",
                    processed_input
                )
                print(
                    "Match Type: EXACT MATCH"
                )
                print(
                    "Matched Question:",
                    question
                )
                print("-------------------")

                return self.answers[i]

        # TF-IDF similarity
        user_vector = self.vectorizer.transform(
            [processed_input]
        )

        similarity_scores = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        best_match_index = (
            similarity_scores.argmax()
        )

        confidence = (
            similarity_scores[
                0
            ][best_match_index]
        )

        best_question = self.questions[
            best_match_index
        ]

        print("\n-------------------")
        print(
            "User Input:",
            user_input
        )
        print(
            "Processed Input:",
            processed_input
        )
        print(
            "Confidence:",
            round(confidence, 3)
        )
        print(
            "Best Question:",
            best_question
        )
        print(
            "Match Type: TF-IDF"
        )
        print("-------------------")

        # Low-confidence fallback
        if confidence < 0.25:

            return (
                "Sorry, I couldn't find "
                "information about that. "
                "Please ask a question related "
                "to SPMVV or B.Tech."
            )

        return self.answers[
            best_match_index
        ]
