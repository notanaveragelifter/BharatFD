from django.core.cache import cache

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        queryset = cache.get(cache_key)

        if not queryset:
            queryset = FAQ.objects.all()
            for faq in queryset:
                faq.question = faq.get_translated_question(lang)
                faq.answer = faq.get_translated_answer(lang)
            cache.set(cache_key, queryset, timeout=60 * 15)  # Cache for 15 minutes
        return queryset