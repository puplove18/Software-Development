/*
This exercise will focus on makefiles exclusively. To begin with, create an empty directory and open a file
called Makefile in your favourite editor. Enter the following content. (Remember to use tabs to indent!)

  hello:
    @echo Hello world!

Save the file. What will happen when you execute make in that directory? Why? Try it out!
Create a file called hello in the same directory (e.g. with touch hello). What happens if you execute
make hello? Why? Fix the problem without renaming / deleting the file hello.
Now, we want to use a Makefile to bake a cake. Start with the following Makefile:

  wheat:
    @echo Growing wheat
    touch wheat
  
  flour: # Flour can only be made if we have wheat
    @echo Making flour
    # When producing flour (create the file), use up (delete) the wheat
  
  sugar:
    # Buy sugar
    
  eggs:
    # Buy eggs
  
  butter:
    # Buy butter
  
  cake: # A cake needs flour, sugar, butter, eggs (and more, but lets simplify things)
    # When making the cake, use up the ingredients
    touch mess

Complete the makefile so that make cake correctly produces a cake. If you make flour sugar eggs,
these three files should exist, and make cake should use them up without recreating them. Getting /
producing an ingredient should print Making XY (or similar) on the console. Remember: To create a file,
use e.g. touch <file>, to delete it rm <file>.
Create a target eat that eats the cake and a target bake that does everything that is necessary to produce
a cake. In particular make bake should produce a cake even if the file bake exists.
Create a target clean that removes mess if it exists (but don’t bake a cake just to make a mess), and
clean_all that removes both mess and cake :(.
Finally, make sure that just running make bakes a cake.
In case you want to learn more, there are numerous tutorials on makefiles online, for example https:
//makefiletutorial.com/.
*/


bake: cake

wheat:
  @echo Growing wheat
  touch wheat

flour: wheat
  @echo Making flour
  touch flour
  rm wheat

sugar:
  @echo Buy sugar
  touch sugar
eggs:
  @echo Buy eggs
  touch eggs
butter:
  @echo Buy butter
  touch butter

cake: flour sugar butter eggs
  @echo Making cake!
  em flour sugar butter eggs
  touch cake mess

.PHONY: bake






