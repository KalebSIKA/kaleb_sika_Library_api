# Full API mini_projetc
this api allows us to collect existing books and categories for various uses, to add new categories as well as new books, to modify or even supress certain books
## Getting Started

### Installing Dependencies

#### Python 3.8.5
#### pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/livres(books)_api` directory and running:

```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the livres(books)_database.sql file provided. From the backend folder in terminal run:
```bash
psql projetflask_database < projetflask.sql
```

## Running the server

From within the `Library_api` directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

```bash
export FLASK_APP=Nancy.py
export FLASK_ENV=development
flask run
```
To run the server on Windows, execute:

```bash
set FLASK_APP=Nancy.py
set FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format:
{
    "success":False
    "error": 400
    "message":"Bad request
}

The API will return four error types when requests fail:
. 400: Bad request
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## GET/livres

    GENERAL:
        This endpoints returns a list of livres object, success value, total number of the livres. 
    
        
    SAMPLE: curl http://localhost:5000/livres

        {
    "": [
        {
            "auteur": "Jacques Pessis, Claude Lemesle",
            "categorie_id": 1,
            "date_publication": "Fri, 15 Oct 2021 00:00:00 GMT",
            "editeur": "Archipel",
            "id": 1,
            "isbn": " 978-2-8098-4260-9",
            "titre": "Bécaud - On vient te chercher"
        },
        {
            "auteur": " Hit the Road",
            "categorie_id": 1,
            "date_publication": "Wed, 15 Dec 2021 00:00:00 GMT",
            "editeur": "Editions du Chêne",
            "id": 2,
            "isbn": "978-2-8123-2110-8",
            "titre": "Infiltrés"
        },
        {
            "auteur": "Vex King",
            "categorie_id": 2,
            "date_publication": "Sat, 12 Jun 2021 00:00:00 GMT",
            "editeur": "Pocket",
            "id": 3,
            "isbn": " 978-2-2663-1489-3",
            "titre": "Cultivez l'énergie positive"
        },
        {
            "auteur": " Elisa Brune",
            "categorie_id": 2,
            "date_publication": "Fri, 05 Mar 2021 00:00:00 GMT",
            "editeur": "Odile Jacob",
            "id": 4,
            "isbn": "978-2-7381-5232-9",
            "titre": "La Révolution du plaisir féminin: Sexualité et orgasme"
        },
        {
            "auteur": "Mathieu Slama",
            "categorie_id": 3,
            "date_publication": "Thu, 20 Jan 2022 00:00:00 GMT",
            "editeur": "Presses de la Cité",
            "id": 5,
            "isbn": "978-2-2581-9777-0",
            "titre": "Adieu la liberté"
        },
        {
            "auteur": " Hubert Prolongeau",
            "categorie_id": 3,
            "date_publication": "Wed, 19 Jan 2022 00:00:00 GMT",
            "editeur": "Flammarion",
            "id": 6,
            "isbn": "978-2-0802-8026-8",
            "titre": "Une haine française"
        },
        {
            "auteur": "Jean Yanne",
            "categorie_id": 4,
            "date_publication": "Fri, 26 Nov 2021 00:00:00 GMT",
            "editeur": "Cherche Midi",
            "id": 7,
            "isbn": "978-2-7491-6896-8",
            "titre": "Je vais m'en farcir quelques-uns !"
        },
        {
            "auteur": " Philippe Bouvard",
            "categorie_id": 4,
            "date_publication": "Thu, 28 Oct 2021 00:00:00 GMT",
            "editeur": "Archipel",
            "id": 8,
            "isbn": "978-2-8098-4256-2",
            "titre": "On s'en souviendra !"
        },
        {
            "auteur": "Ariana Godoy",
            "categorie_id": 5,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "Hachette Romans",
            "id": 9,
            "isbn": " 978-2-0171-4772-5",
            "titre": "À travers ma fenêtre"
        },
        {
            "auteur": "Anita Diamant",
            "categorie_id": 5,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": " Charleston",
            "id": 10,
            "isbn": "978-2-3681-2736-0",
            "titre": "La Tente rouge"
        },
        {
            "auteur": "Tracy Long",
            "categorie_id": 6,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "Albin Michel",
            "id": 11,
            "isbn": "978-2-2264-7053-9",
            "titre": "Les Clés de l'ésotérisme - Chamanisme"
        },
        {
            "auteur": "Frédéric Nef",
            "categorie_id": 6,
            "date_publication": "Wed, 24 Nov 2021 00:00:00 GMT",
            "editeur": "Cerf",
            "id": 12,
            "isbn": "978-2-2041-4625-8",
            "titre": "La mort n'existe pas"
        },
        {
            "auteur": " Thierry Courtin",
            "categorie_id": 7,
            "date_publication": "Mon, 10 Jan 2022 00:00:00 GMT",
            "editeur": " Nathan",
            "id": 13,
            "isbn": "978-2-0919-3556-0",
            "titre": "T'choupi Mon cahier ardoise - Ma petite section - dès 3 ans"
        },
        {
            "auteur": "Christophe Bernicot, Thomas Roy, Jean-Christophe Tisserand, Nadine Valade",
            "categorie_id": 7,
            "date_publication": "Sun, 21 Nov 2021 00:00:00 GMT",
            "editeur": "Ellipses",
            "id": 14,
            "isbn": "978-2-3400-4886-7",
            "titre": "Chimie PCSI - Nouveaux programmes"
        },
        {
            "auteur": "Molière",
            "categorie_id": 8,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": " Flammarion",
            "id": 15,
            "isbn": "978-2-0802-6878-5",
            "titre": "L'avare"
        },
        {
            "auteur": "Molière",
            "categorie_id": 8,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": " Flammarion",
            "id": 16,
            "isbn": " 978-2-0802-6880-8",
            "titre": "Le misanthrope"
        },
        {
            "auteur": "Zidrou",
            "categorie_id": 9,
            "date_publication": "Fri, 11 Feb 2022 00:00:00 GMT",
            "editeur": "Lombard",
            "id": 17,
            "isbn": "978-2-8036-7956-0",
            "titre": "Un amour de génie"
        },
        {
            "auteur": "XXX",
            "categorie_id": 9,
            "date_publication": "Fri, 11 Feb 2022 00:00:00 GMT",
            "editeur": " Urban Comics Editions ",
            "id": 18,
            "isbn": "979-1-0268-2035-2",
            "titre": "Batman Arkham : L'Épouvantail"
        },
        {
            "auteur": "Jean-Joseph Julaud",
            "categorie_id": 10,
            "date_publication": "Sun, 10 Oct 2021 00:00:00 GMT",
            "editeur": "First",
            "id": 19,
            "isbn": "978-2-4120-7308-7",
            "titre": "Le Petit Livre de la grammaire facile, 2e édition"
        },
        {
            "auteur": "Anne Abeille, Danièle Godard, Antoine Gautier, Annie Delaveau",
            "categorie_id": 10,
            "date_publication": "Sun, 10 Oct 2021 00:00:00 GMT",
            "editeur": " Actes Sud ",
            "id": 20,
            "isbn": "978-2-3301-4239-1",
            "titre": "La Grande grammaire du français"
        },
        {
            "auteur": "Patrick Dussossoy",
            "categorie_id": 11,
            "date_publication": "Fri, 15 Oct 2021 00:00:00 GMT",
            "editeur": "Gereso",
            "id": 21,
            "isbn": "979-1-0397-0004-7",
            "titre": "Le business plan en pratique"
        },
        {
            "auteur": "Aurélie Stefani",
            "categorie_id": 11,
            "date_publication": "Sat, 20 Nov 2021 00:00:00 GMT",
            "editeur": "Opportun",
            "id": 22,
            "isbn": "978-2-3801-5150-3",
            "titre": "J'arrête de boire en 30 jours"
        },
        {
            "auteur": "Robert C. Martin",
            "categorie_id": 12,
            "date_publication": "Wed, 11 Nov 2020 00:00:00 GMT",
            "editeur": "Pearson",
            "id": 23,
            "isbn": "978-2-3260-0267-8",
            "titre": "Architecture logicielle propre"
        },
        {
            "auteur": "Dan Gookin",
            "categorie_id": 12,
            "date_publication": "Sun, 13 Feb 2022 00:00:00 GMT",
            "editeur": "First Interactive",
            "id": 24,
            "isbn": "978-2-4120-7350-6",
            "titre": "Word 2021 pour les Nuls, grand format"
        },
        {
            "auteur": "Lisa Kleypas",
            "categorie_id": 13,
            "date_publication": "Wed, 01 Dec 2021 00:00:00 GMT",
            "editeur": "J'ai lu",
            "id": 25,
            "isbn": "978-2-2901-4505-0",
            "titre": "La ronde des saisons -5- Retrouvailles"
        },
        {
            "auteur": "Elle Seveno",
            "categorie_id": 13,
            "date_publication": "Wed, 10 Nov 2021 00:00:00 GMT",
            "editeur": "Hugo Roman",
            "id": 26,
            "isbn": "978-2-7556-8847-4",
            "titre": "Nos rêves en parallèle"
        },
        {
            "auteur": "Anne Ancelin Schützenberger",
            "categorie_id": 14,
            "date_publication": "Wed, 02 Feb 2022 00:00:00 GMT",
            "editeur": "Editions Payot & Rivages",
            "id": 27,
            "isbn": "978-2-2289-3018-5",
            "titre": "Le psychodrame"
        },
        {
            "auteur": "Jean-Luc Nancy",
            "categorie_id": 14,
            "date_publication": "Thu, 20 Jan 2022 00:00:00 GMT",
            "editeur": "De L'Aube",
            "id": 28,
            "isbn": " 978-2-8159-4770-1",
            "titre": "C'est quoi penser par soi-même ?"
        },
        {
            "auteur": "Nos futurs",
            "categorie_id": 15,
            "date_publication": "Thu, 21 Jan 2021 00:00:00 GMT",
            "editeur": "Actusf",
            "id": 29,
            "isbn": " 978-2-3768-6437-0",
            "titre": "Nos futurs"
        },
        {
            "auteur": "Gilberto Villarroel",
            "categorie_id": 15,
            "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": " Pocket",
            "id": 30,
            "isbn": "978-2-2663-2229-4",
            "titre": "Lord Cochrane vs l'Ordre des catacombes"
        },
        {
            "auteur": "Lonely Planet, Peter Dragicevich, Anthony Ham, Jessica Lee",
            "categorie_id": 16,
            "date_publication": "Tue, 18 Jan 2022 00:00:00 GMT",
            "editeur": " Lonely Planet ",
            "id": 31,
            "isbn": "978-1-7886-8076-9",
            "titre": "Lonely Planet Croatia"
        },
        {
            "auteur": "Nancy Lakt KOFFETO",
            "categorie_id": 16,
            "date_publication": "Wed, 26 Jan 2022 00:00:00 GMT",
            "editeur": "Hachette Tourisme",
            "id": 32,
            "isbn": "978-2-0171-7202-4",
            "titre": "Guide du Routard Canaries 2022/23"
        },
        {
            "auteur": "Katia Bricka",
            "categorie_id": 17,
            "date_publication": "Tue, 25 Jan 2022 00:00:00 GMT",
            "editeur": "Modus Vivendi",
            "id": 33,
            "isbn": " 978-2-8977-6178-3",
            "titre": "La recette parfaite: Mealprep végane"
        },
        {
            "auteur": "Nancy Lakt KOFFETO",
            "categorie_id": 17,
            "date_publication": "Sat, 12 Feb 2022 00:00:00 GMT",
            "editeur": "Papatchka",
            "id": 34,
            "isbn": " 978-2-2212-5561-2",
            "titre": "L'ingenieurie culinaire de Nanatchka"
        },
        {
            "auteur": "Jean-Luc Pissaloux, Anne Rainaud",
            "categorie_id": 18,
            "date_publication": "Tue, 14 Dec 2021 00:00:00 GMT",
            "editeur": "Bruylant Edition",
            "id": 35,
            "isbn": "978-2-8027-6247-8",
            "titre": "Droit du nucléaire"
        },
        {
            "auteur": "Pascal Picq",
            "categorie_id": 18,
            "date_publication": "Tue, 23 Nov 2021 00:00:00 GMT",
            "editeur": "Eyrolles",
            "id": 36,
            "isbn": "978-2-4160-0487-2",
            "titre": "Un paléoanthropologue dans l'entreprise:S'adapter et innover pour survivre"
        },
        {
            "auteur": "Mary Beard",
            "categorie_id": 19,
            "date_publication": "Thu, 03 Feb 2022 00:00:00 GMT",
            "editeur": " Perrin",
            "id": 37,
            "isbn": "978-2-2620-9741-7",
            "titre": "S.P.Q.R."
        },
        {
            "auteur": "Charles-Eloi Vial",
            "categorie_id": 19,
            "date_publication": "Thu, 13 Jan 2022 00:00:00 GMT",
            "editeur": "Perrin",
            "id": 38,
            "isbn": "978-2-2620-9457-7",
            "titre": "Le siècle des chutes"
        },
        {
            "auteur": "Jean-Joseph Julaud",
            "categorie_id": 20,
            "date_publication": "Thu, 13 Jan 2022 00:00:00 GMT",
            "editeur": " First",
            "id": 39,
            "isbn": "978-2-4120-7674-3",
            "titre": "Le petit livre des grandes dates de l'Histoire de France"
        },
        {
            "auteur": "SUTHERLAND/SUTHERLAND",
            "categorie_id": 20,
            "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": "Gallimard",
            "id": 40,
            "isbn": "978-2-0751-6463-4",
            "titre": "SOS CREATURES FANTASTIQUES 2 T2: LE PROCES DU DRAGON"
        },
        {
            "auteur": "Mike Nicol",
            "categorie_id": 21,
            "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": "Gallimard",
            "id": 41,
            "isbn": "978-2-0729-0598-8",
            "titre": "Infiltrée"
        },
        {
            "auteur": "Patrice Lopès, François-Xavier Poudat",
            "categorie_id": 22,
            "date_publication": "Wed, 12 Jan 2022 00:00:00 GMT",
            "editeur": "Elsevier Masson",
            "id": 43,
            "isbn": "978-2-2947-7438-6",
            "titre": "Manuel de sexologie"
        },
        {
            "auteur": "Gabriel Perlemuter",
            "categorie_id": 22,
            "date_publication": "Tue, 02 Nov 2021 00:00:00 GMT",
            "editeur": "Pocket",
            "id": 44,
            "isbn": "978-2-2663-1983-6",
            "titre": "De l'intestin au cerveau"
        },
        {
            "auteur": "Zlatan Ibrahimovic",
            "categorie_id": 23,
            "date_publication": "Tue, 26 Jan 2021 00:00:00 GMT",
            "editeur": "Flammarion",
            "id": 45,
            "isbn": "978-2-0802-7052-8",
            "titre": "Adrénaline"
        },
        {
            "auteur": " L'Equipe",
            "categorie_id": 23,
            "date_publication": "Sat, 25 Dec 2021 00:00:00 GMT",
            "editeur": "Solar",
            "id": 46,
            "isbn": "978-2-2631-7232-8",
            "titre": "Les années Federer"
        },
        {
            "auteur": "Danü Danquigny",
            "categorie_id": 21,
            "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": "Gallimard ",
            "id": 42,
            "isbn": "978-2-7491-7253-8",
            "titre": "Peter punk au pays des merveilles"
        }
    ],
    "success": true,
    "total_": 46
}

. ## DELETE/categorie)

    GENERAL:
        Delete the categorie of the given ID if it exists. Return the id of the deleted categorie, success value, total of (books) a

        Results are paginated in groups of 25. include a request argument to choose page number, starting from 1.

        SAMPLE: curl -X DELETE http://localhost:5000/categories/25
```
        {
        'success': True,
        'delete successfully': 25,
         }
        {
    "Categorie": [
        {
            "id": 1,
            "libelle_categorie": "Art et cinema"
        },
        {
            "id": 2,
            "libelle_categorie": "Developpement personnel"
        },
        {
            "id": 3,
            "libelle_categorie": "Essais et document"
        },
        {
            "id": 4,
            "libelle_categorie": "Humour"
        },
        {
            "id": 6,
            "libelle_categorie": "Religion et spiritualité"
        },
        {
            "id": 7,
            "libelle_categorie": "Scolaire"
        },
        {
            "id": 8,
            "libelle_categorie": "Théatre"
        },
        {
            "id": 9,
            "libelle_categorie": "Bandes dessinées"
        },
        {
            "id": 10,
            "libelle_categorie": "Dictionnaire & Langues"
        },
        {
            "id": 11,
            "libelle_categorie": "Guide Pratiques"
        },
        {
            "id": 12,
            "libelle_categorie": "Informatique et Internet"
        },
        {
            "id": 13,
            "libelle_categorie": "Literrature sentimentale"
        },
        {
            "id": 14,
            "libelle_categorie": "Science sociales"
        },
        {
            "id": 15,
            "libelle_categorie": "SF,Fantasy"
        },
        {
            "id": 16,
            "libelle_categorie": "Tourisme et Voyages"
        },
        {
            "id": 17,
            "libelle_categorie": "Cuisine"
        },
        {
            "id": 18,
            "libelle_categorie": "Droit & Economie"
        },
        {
            "id": 19,
            "libelle_categorie": "Histoire"
        },
        {
            "id": 20,
            "libelle_categorie": "Jeunesse"
        },
        {
            "id": 21,
            "libelle_categorie": "Policier,suspense,thrillers"
        },
        {
            "id": 22,
            "libelle_categorie": "Sciences,techniques & médecine"
        },
        {
            "id": 23,
            "libelle_categorie": "Sport loisirs et vie pratique"
        },
        {
            "id": 5,
            "libelle_categorie": "Littérature"
        },
        {
            "id": 24,
            "libelle_categorie": "Ma beauté legendaire"
        }
    ],
    "success": true,
    "total_categories": 24
}
```
. ##PATCH/livres/id
  GENERAL:
  This endpoint is used to update a primary_color of plant
  We return a livre(book) which we update

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/livres/42-H "Content-Type:application/json" -d "{"titre": "Peter punk au pays des merveilles"}"
  ```
  ```
   {
    "auteur": "Danü Danquigny",
    "categorie_id": 21,
    "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
    "editeur": "Gallimard ",
    "id": 42,
    "isbn": "978-2-7491-7253-8",
    "titre": "Peter punk au pays des merveilles"
   }
    ```

. ## POST/categories

    GENERAL:    
    This endpoint is used to create a new plant or to search for a plant in relation to the terms contained in the livres(books).
    When the searchTerm parameter is passed from the json, the endpoint performs the search. Otherwise, it is the creation of a new question.
    In the case of the creation of a new question:
    We return the ID of the new plant created, the plant that was created, the list of plant and the number of livres(books).

    SAMPLE.....For Search:
    ```
    curl -X POST http://localhost:5000/categories -H "Content-Type:application/json" -d "{"search":"title"}"
    ```

                

    SAMPLE.....For create

    curl -X POST http://localhost:5000/categories -H "Content-Type:application/json" -d "{"id": 24,"libelle_categorie": "Ma beauté legendaire"}"
```
    {
    "Categorie": [
        {
            "id": 1,
            "libelle_categorie": "Art et cinema"
        },
        {
            "id": 2,
            "libelle_categorie": "Developpement personnel"
        },
        {
            "id": 3,
            "libelle_categorie": "Essais et document"
        },
        {
            "id": 4,
            "libelle_categorie": "Humour"
        },
        {
            "id": 6,
            "libelle_categorie": "Religion et spiritualité"
        },
        {
            "id": 7,
            "libelle_categorie": "Scolaire"
        },
        {
            "id": 8,
            "libelle_categorie": "Théatre"
        },
        {
            "id": 9,
            "libelle_categorie": "Bandes dessinées"
        },
        {
            "id": 10,
            "libelle_categorie": "Dictionnaire & Langues"
        },
        {
            "id": 11,
            "libelle_categorie": "Guide Pratiques"
        },
        {
            "id": 12,
            "libelle_categorie": "Informatique et Internet"
        },
        {
            "id": 13,
            "libelle_categorie": "Literrature sentimentale"
        },
        {
            "id": 14,
            "libelle_categorie": "Science sociales"
        },
        {
            "id": 15,
            "libelle_categorie": "SF,Fantasy"
        },
        {
            "id": 16,
            "libelle_categorie": "Tourisme et Voyages"
        },
        {
            "id": 17,
            "libelle_categorie": "Cuisine"
        },
        {
            "id": 18,
            "libelle_categorie": "Droit & Economie"
        },
        {
            "id": 19,
            "libelle_categorie": "Histoire"
        },
        {
            "id": 20,
            "libelle_categorie": "Jeunesse"
        },
        {
            "id": 21,
            "libelle_categorie": "Policier,suspense,thrillers"
        },
        {
            "id": 22,
            "libelle_categorie": "Sciences,techniques & médecine"
        },
        {
            "id": 23,
            "libelle_categorie": "Sport loisirs et vie pratique"
        },
        {
            "id": 5,
            "libelle_categorie": "Littérature"
        },
        {
            "id": 24,
            "libelle_categorie": "Ma beauté legendaire"
        }
    ],
    "success": true,
    "total_categories": 24
}
```      


## Testing
To run the tests, run
```
dropdb livres_database
createdb livres_database
psql livres_database_test < livres_database.sql
python test_flaskr.py
```