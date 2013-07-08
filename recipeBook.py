from datetime import date


class recipeBook:
	

	def _init_ (spiderman, name, year = date.today().year, desc = "Lvl 37 Recipe Book of Enchanted Flavour"):
		spiderman.name = name
		spiderman.year = year
		spiderman.description = desc
		spiderman.recipes = []
		spiderman.coverPic = None
		spiderman.ToC = []  #will hold the dynamic GUI pages
		spiderman.tags = ();
		
		

	#called from the GUI, this adds the new recipe to the recipeBook
	def addRecipe(space, recipe):
		space.recipes.append(recipe)
		space.tags.add(recipe.category)
		space.genToC()
	
	#similarly, removes recipes from recipeBook
	def removeRecipe(spiderman, recipe):
		spiderman.recipes.remove(recipe)
		spiderman.genToC()


	# users can select a photo to be the cover of their recipeBook.  It's stored here
	def addCover(spiderman, picLocation):
		spiderman.coverPic = picLocation

	#dynamically creates the recipe book's table of contents
	def genToC(self):

		pages = len(recipes)
		if (pages > 0)

	#search and filter functions

	#returns a list of recipes whose name contains the provided text
	def nameSearch(self, text):
		return results = [x for x in self.recipes if text in x.name]

	#returns a set of recipes that match the provided tags
	def tagFilter(self, tags):
		i = 0
		j = 0
		while (i < len(tags)
			while(j < len(self.recipes))
				if ( self.recipes[j].category == tags[i])
					results.add(self.recipes[j])
				j++
			
			i++
		
		return results
		



	

	
