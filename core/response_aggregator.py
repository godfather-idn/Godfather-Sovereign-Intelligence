class ResponseAggregator:

    @staticmethod
    def combine(results):

        responses = []

        for result in results:
            responses.append(result["response"])

        return "\n\n".join(responses)