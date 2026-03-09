def get_recommendations(disease, severity="medium"):

    recommendations = {

    "acne":{

        "lifestyle":[
        "Wash face twice daily",
        "Avoid oily food",
        "Reduce stress"
        ],

        "home_remedies":[
        "Apply aloe vera gel",
        "Use honey mask",
        "Tea tree oil"
        ],

        "medical":[
        "Benzoyl peroxide",
        "Salicylic acid creams"
        ]
    },

    "eczema":{

        "lifestyle":[
        "Avoid harsh soaps",
        "Moisturize frequently"
        ],

        "home_remedies":[
        "Coconut oil",
        "Oatmeal bath"
        ],

        "medical":[
        "Hydrocortisone cream"
        ]
    },

    "psoriasis":{

        "lifestyle":[
        "Avoid alcohol",
        "Reduce stress"
        ],

        "home_remedies":[
        "Aloe vera",
        "Dead sea salt bath"
        ],

        "medical":[
        "Topical corticosteroids"
        ]
    }
    }

    return recommendations[disease]