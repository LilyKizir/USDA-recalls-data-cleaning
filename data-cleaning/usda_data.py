import requests

url = "https://www.fsis.usda.gov/fsis/api/recall/v/1?field_states_id=All&field_archive_recall=All&field_closed_date_value=&field_closed_year_id=All&field_risk_level_id=All&field_processing_id=All&field_product_items_value=meat&field_recall_classification_id=All&field_recall_number=&field_recall_reason_id=All&field_recall_type_id=All&field_related_to_outbreak=All&field_summary_value=&field_year_id=All&field_translation_language=All"

headers = {
    "User-Agent": "data analytics personal project @ thedataschool (contact:)"
}

response = requests.get(url,headers=headers)
print(response)