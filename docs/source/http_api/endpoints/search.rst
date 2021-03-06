*************************
Retrieve Talks via Search
*************************

.. http:get:: /talks/search

    Search for Talks

    **Example request**:

    .. sourcecode:: http

		GET /api/talks/search?from=today&topic=X HTTP/1.1
		Host: talks.ox.ac.uk
		Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "_links": {
                "self": {
                    "href": "http://talks.ox.ac.uk/api/talks/search?from=01/01/01"
                },
                "next": null,
                "prev": null
            },
            "_embedded":
                {
                    "talks": [
                    {
                        "_links": {
                            "self": {
                                "href": "/api/talks/fa67d13a-f17d-471d-b8cc-33b3d7759956"
                            },
                            "talks_page": {
                                "href": "/talks/id/fa67d13a-f17d-471d-b8cc-33b3d7759956/"
                            }

                        },
                        "title": "What can babies with Down syndrome possibly tell us about Alzheimer's dementia in adults?",
                        "start": "2015-01-29T18:00:00Z",
                        "end": "2015-01-29T19:00:00Z",
                        "formatted_date": "29 January 2015, 18:00",
                        "formatted_time": "18:00",
                        "description": "It may seem paradoxical to focus on babies ...",
                        "_embedded":
                        {
                            "speakers": [ ],
                            "venue": {
                                "_links": {
                                    "self": {
                                        "href": "//api.m.ox.ac.uk/places/oxpoints:50009121"
                                    }
                                },
                                "name": "Mary Gray Allen Building",
                                "map_link": "//maps.ox.ac.uk/#/places/oxpoints:50009121"

                            },
                            "organising_department": null,
                            "topics": [
                                {
                                    "uri": "http://id.worldcat.org/fast/806532",
                                    "label": "Alzheimer's disease"
                                }, {
                                    "uri": "http://id.worldcat.org/fast/890050",
                                    "label": "Dementia"
                                }
                            ]
                        }
                    }
                    ]
                }
            }


    The response can be either in XML or JSON dependent on the 'accept' header in the request.

    :statuscode 200: query found
    :statuscode 400: Bad request (could happen if some parameters are missing or incorrectly formed such as `from`)
    :statuscode 503: Service not available


Parameters Reference
====================


from : date string (`'yyyy-mm-dd'`), **required**
     * Start date for the list of talks.
     * Format as :code:`yyyy-mm-dd` or :code:`dd/mm/yy` (deprecated)
     * Or use the keyword :code:`'today'` to get upcoming talks

to : date string (`'yyyy-mm-dd'`), optional
    * End date for the list of talks.
    * Format :code:`yyyy-mm-dd` or :code:`dd/mm/yy` (deprecated)
    * Or use :code:`plus[n]` for the next [n] days (e.g.: plus7)
    * Note that the issue with the end time (assumed to be 00:00 not 23:59) has now been resolved

subdepartments : boolean, optional
    * If true, include all sub-organisations of the specified department within the search (see organising_department below)
    * Defaults to **true**.

count : integer, optional
    * Number of talks to return per page


The parameters below can each be repeated multiple times

speaker : speaker slug as string, optional
         * For a list of talks by a specific speaker
         * Format :code:`f8ecded3-d2af-4585-bd3b-5cd7440795b9`

series : series slug as string, optional
         * For a list of talks belonging to a specific series
         * Format :code:`f8ecded3-d2af-4585-bd3b-5cd7440795b9`

venue : Oxpoints ID as string, optional
       * For a list of talks in a specific venues
       * Format :code:`oxpoints:59444038`

organising_department : Oxpoints ID as string, optional
        * For a list of talks in a specific organising department
        * Format :code:`oxpoints:23232596`
        * use the subdepartments parameter (see above) to include sub-organisations of the department

topic : FAST topic URI as string, optional
        * For a list of talks on a topics
        * Format :code:`http://id.worldcat.org/fast/1097048`
