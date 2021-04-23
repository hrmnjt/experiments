/*
Package twofer implements a library to send sharing agreement

`Two-fer` or `2-fer` is short for two for one. One for you and one for me.

Given a name, return a string with the message:

```text
One for X, one for me.
```

Where X is the given name.

However, if the name is missing, return the string:

```text
One for you, one for me.
```

Here are some examples:

|Name    |String to return
|:-------|:------------------
|Alice   |One for Alice, one for me.
|Bob     |One for Bob, one for me.
|        |One for you, one for me.
|Zaphod  |One for Zaphod, one for me.

*/
package twofer

import "fmt"

// ShareWith accepts a string - name which is returned as per the
// string interpolation logic applied
func ShareWith(name string) string {

	two_for_one := ""
	if len(name) == 0 {
		two_for_one = "One for you, one for me."
	} else {
		two_for_one = fmt.Sprintf("One for %s, one for me.", name)
	}
	return two_for_one
}
