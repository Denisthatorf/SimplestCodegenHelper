## Very very simple code generator


Keywords :

* repeat - start repeat session
* end - end repeat session

Rules :

* everything that starts with $$ and continues with a word or '_' is a variable name and will be changed to the name in the input dictionary
* everething outside repeat writes without variable name changing
* "repeat" must end with "end"
* now you can't put repeat inside repeat

### eventCallback.hpp -> eventCallback.out.hpp - easy example