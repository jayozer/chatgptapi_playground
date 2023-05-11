from outscraper import ApiClient

api_client = ApiClient(api_key='SECRET_API_KEY')
reviews_response = api_client.google_maps_business_reviews(
    'Novato Pediatric Dentistry, Novato, CA', limit=57, language='en')