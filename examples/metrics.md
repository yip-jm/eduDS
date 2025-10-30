### Knowledge Extraction Evaluation Metrics
| Metric Category | Sub-metric | Definition | Scoring Range | Calculation Formula |
|-----------------|------------|------------|---------------|--------------------|
| Retrieval Score | - | Measures semantic alignment between retrieved chunks, user questions, and reference key information. Calculates max similarity for each reference sentence/question with retrieved chunks, then averages. | 0-5 | Average of max similarities across all reference sentences and input questions |
| Generation Score | Faithfulness | Checks if generated content is strictly grounded in retrieved context | 0-5 | - |
| | Accuracy | Measures correctness of all key facts, concepts, and definitions | 0-5 | - |
| | Completeness | Evaluates if all required aspects of the question are addressed (e.g., definition, significance, strengths, weaknesses) | 0-5 | - |
| | - | Composite score of faithfulness, accuracy, and completeness | 0-5 | (Faithfulness + Accuracy + Completeness) / 3 |
| Overall Score | - | Weighted sum of retrieval and generation scores | 0-5 | 0.4\*Retrieval Score + 0.6\*Generation Score |

---

### Story Generation Evaluation Metrics
| Metric Category | Sub-metric | Definition | Scoring Range | Calculation Formula |
|-----------------|------------|------------|---------------|--------------------|
| Story Quality Score | Structure | Whether the story follows "Problem → Solution → Impact" structure | 0-5 | - |
| | Factual Accuracy | Whether story content is consistent with the source concept | 0-5 | - |
| | Narrative Coherence | Whether the story flows logically without contradictions | 0-5 | - |
| | Educational Engagement | Whether it includes teaching hooks (e.g., questions, analogies) | 0-5 | - |
| | Fluency & Consistency | Whether the text has grammar issues or hallucinations | 0-5 | - |
| | - | Composite score of the 5 sub-metrics | 0-5 | Sum of 5 Metrics / 5 |
| Activity Quality Score | Narrative Grounding | Whether the activity is meaningfully embedded in the story context (characters, plot tension, moral dilemma) | 0-5 | - |
| | Classroom Applicability Usability | Whether the activity can be directly used in classrooms to promote engagement, critical thinking, or collaborative exploration | 0-5 | - |
| | - | Composite score of the 2 sub-metrics | 0-5 | Sum of 2 Metrics / 2 |
| Overall Score | - | Average of story quality and activity quality scores | 0-5 | (Activity Quality Score + Story Quality Score) / 2 |

> Note: All evaluations are performed by DeepSeek-V3 with detailed scoring rubrics (3-4 sub-criteria per task). Final scores are averages of respective criteria scores.

