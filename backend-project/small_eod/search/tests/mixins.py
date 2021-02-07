class SearchQueryMixin:
    def get_response_for_query(self, query):
        self.login_required()
        return self.client.get(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data={"query": query},
        )

    def assertResultEqual(self, response, items):
        self.assertEqual(response.status_code, 200, response.json())
        item = response.json()["results"]
        self.assertEqual(len(item), len(items))
        for i, el in enumerate(items):
            self.assertEqual(item[i]["id"], el.pk)

    def test_search_by_pk(self):
        # should support always filter by pk
        second = self.factory_class()
        response = self.get_response_for_query(f"id:{second.pk}")
        self.assertResultEqual(response, [second])

    def test_search_invalid(self):
        self.login_required()
        response = self.get_response_for_query("id:")
        self.assertEqual(response.status_code, 400, response.json())
        item = response.json()
        self.assertEqual(
            item["query"][0],
            "Expected end of text, found ':'  (at char 2), (line:1, col:3)",
        )
