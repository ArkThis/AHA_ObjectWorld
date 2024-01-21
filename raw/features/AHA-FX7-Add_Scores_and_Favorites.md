## Add score to "name=value" pairs

To cover the following use-cases:

  * With multiple, identical "name=" entries, one can set a preferred "default".
  * Wrong metadata may be scored "badly" if desired.

The score/weight may be stored in a string syntax in the "name", to avoid an additional column on the basic "name=value" level.
Actually, one may even consider just a numeric "sort index" added to the "name".

Example:

  * title1.0 = default title.
  * title2.100000000 = probably bogus title.

Queries shall be possible in the following intentions:

  * Get default "title":
    `if (object.title == '...') and sortindex == 0 ...`
  * Quick-check if more than 1 "title" is set:
    `if exist (object.title2) ...`
  * Also check if there is more than 1 "title" set:
    `if count(title)>1 ...`

And so on.

