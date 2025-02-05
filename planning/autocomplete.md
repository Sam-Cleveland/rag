# Auto-Complete Sentence

### **Purpose**: 
Generate relevant sentence completions based on context sentences and optional sentence type

### **Endpoint**: POST /autocomplete

### **Description**: 
This endpoint takes a partial sentence and a list of context sentences, and returns a list of potential completions or replacements for the sentence. The completions are generated based on the context sentences and ordered by relevance. Optionally, you can specify the type/purpose of the sentence to help guide the completion suggestions.
# 

**Request Body (JSON)**:
  ```json
  {
    "user_sentence": "string",
    "context_sentences": ["string"],
    "sentence_type": "string (optional)"
  }
  ```

**Parameters**:
- `user_sentence`: The sentence to auto-complete
- `context_sentences`: The list of context sentences
- `sentence_type`: The purpose of the sentence (optional) i.e. "Prayer Request", "Gratitude"

**Response Body (JSON)**:
- Success (200 OK):
  ```json
  {
    "completions": "array of strings",
  }
  ```

**Fields**:
- `completion`: The list of completions/replacements for the `user_sentence` ordered by relevance
