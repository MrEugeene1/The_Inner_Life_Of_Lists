# The Inner Life of Python Lists

This project explains one of the most important Python concepts:

When you assign one list to another variable, Python does not copy the values.
It copies the reference to the same list object in memory.

Because of that, changing one variable can change what you see through the other variable too.

If you want an actual copy, use slicing or another copy technique.

## Who This Is For

- Beginners: You will build the right mental model early.
- Experienced developers: You get a quick refresher and practical patterns to avoid bugs.

## What This Project Demonstrates

The file innerLifeOfList.py shows three ideas:

1. Reference assignment (surprising behavior)
2. Full list copy using slicing
3. Partial copy using slicing ranges

## 1) Reference Assignment (Not a Copy)

Example:

	list_1 = [1]
	list_2 = list_1
	list_1[0] = 2
	print(list_2)

Output:

	[2]

Why this happens:

- list_2 = list_1 does not create a new list.
- Both names point to the same list in memory.
- Mutating through one name is visible through the other.

Think of it like two labels on one box.

## 2) Full Copy with Slicing

Example:

	list_1 = [1]
	list_2 = list_1[:]
	list_1[0] = 2
	print(list_2)

Output:

	[1]

Why this works:

- list_1[:] creates a new list object.
- The new list gets copied elements.
- list_1 and list_2 now refer to different objects.

## 3) Copying Only Part of a List

General form:

	my_list[start:end]

Rules:

- start is included.
- end is excluded.
- Number of elements is end - start.

Example:

	my_list = [10, 8, 6, 4, 2]
	new_list = my_list[1:3]
	print(new_list)

Output:

	[8, 6]

Explanation:

- Index 1 is included (value 8).
- Index 2 is included (value 6).
- Index 3 is excluded.

## Key Concept to Memorize

For scalar values (like integers), assignment behaves like value passing in everyday use.
For lists and other mutable objects, assignment passes a reference.

This difference causes many real-world bugs in data processing, API payload preparation, and test setup.

## Common Bug Pattern

You expected a backup list, but actually created an alias.

	original = [1, 2, 3]
	backup = original
	original.append(4)

Now backup is also [1, 2, 3, 4].

Safer version:

	backup = original[:]

## Practical Copy Options

- Shallow copy with slicing:

	copied = my_list[:]

- Shallow copy with method:

	copied = my_list.copy()

- Shallow copy with constructor:

	copied = list(my_list)

Note: These are shallow copies. Nested mutable objects are still shared.

## How to Run

From this folder, run:

	py innerLifeOfList.py

## Expected Console Output

You should see:

	[2]
	[1]
	[8, 6]

This sequence proves:

- alias assignment shares one list
- slicing can create an independent copy
- slice ranges extract specific segments

## Quick Reference

- a = b: same list object (alias)
- a = b[:]: new list (shallow copy)
- a = b[start:end]: new sub-list from start to end-1

## License

Educational and personal use.

