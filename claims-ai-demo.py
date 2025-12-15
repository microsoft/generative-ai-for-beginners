def summarize_claim(claim_text):
    """
    Summarize an insurance claim into key facts.
    """
    # Split and clean sentences
    sentences = [s.strip() for s in claim_text.split(".") if s.strip()]
    # Take the first two sentences
    summary = ". ".join(sentences[:2]) + "."
    return summary

# Step 2: Example claim document
claim_document = "On December 10th, 2025, Mr. Ade filed a motor accident claim. His Toyota Corolla was rear-ended at a traffic light in Lagos. The estimated repair cost is ₦1,200,000. No injuries were reported."


# Step 3: Run the summarizer
print("Original Claim Document:")
print(claim_document)
print("\nAI-Generated Summary:")
print(summarize_claim(claim_document))
