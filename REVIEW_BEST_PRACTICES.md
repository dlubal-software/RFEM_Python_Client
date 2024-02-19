# Review Best Practices

## Best practice for the author
* Before submitting the code for review, the code author should perform the review himself. Read the entire code several times carefully. Code should have good structure, documentation and needs to be functional.
* It is a good practice to also check the diff if all changes are in US/Bugfix scope. The diff helps to spot temporary code.
* There needs to be a good reason for modifying code outside of scope.
* It is better to review several small changes than one big change. Smaller changes are easier to navigate and better revised.
* Have the code checked with linter or other type of static code analysis tool before code review.
* On the review board, a brief description of changes, new functions and any notes on the solution needs to be added. The reviewer then finds his way around and understands the code way faster.
* When correcting the code, the author must make changes himself to learn from the mistakes.

## Best practice for reviewer
* New objections to the code can only be raised in the first round of corrections, in the next round of corrections it is possible to raise objections only to what was changed in the given round.
* Ignore who is the author of the code. Even a senior programmer makes mistakes.

## Who should do the review?
* In addition to monitoring the quality of the code, code review has the advantage that at least two programmers have gone through each part of the code and are familiar with it (have awareness).
* It is advisable that the revisions are evenly distributed among the programmers in the team.
* It is advisable that I junior do the revision

## Division of objections into three categories:
* Nitpick - this category includes everything that is not important. Comment formatting etc.
* Blocking - serious offenses that can cause the application to crash, break the existing code, do not meet the requirements of OOP.
* To discuss – Category between Nitpick and Blocking. The code will work correctly even without fixing them. Bad use of libraries, incomplete adherence to architecture, bad naming of things, code structure.
The author must fix all blocking comments, To discuss can be skipped, but he must create a bugfix for them when he fixes them in the future. A nitpick is fine to fix, but not required.

## What to check (in order of priority):
* Serious errors like memory leak, unhandled exceptions, etc.
* Isolation of changes – if the changes do not break some piece of code that is not changed.
* Offenses against PPE and encapsulation, DRY
* Offenses against the coding standard
* Unclear or wrong naming of variables, methods, classes...
* Unnecessarily complex code
* Documentation: whether the more complex parts of the code are properly commented
* Typos in comments and line breaks in the code (cases that are not described in the coding standard

## Communication:
* Be constructive. If you criticize some part of the change, then in addition to the reason why it is good to write how the given thing could be done better and what will be solved by it.
* Don't get personal. Always talk about the code, not the other person's skills. It is better to ask questions than to directly criticize. Because it is very difficult to know all the connections and reasons that led to writing a given piece of code, and there is a greater chance that the author knows it better than you. Even if you're sure, it's better to ask what the reason for this modification is than to just say it's unnecessary. It happens to the other person too, and then he takes it partially as his own idea, and most of all, he doesn't feel that he is being blamed for anything.
* Don't be afraid to brag :-)
