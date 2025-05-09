team_12 = {
  'grade': 'seniors',
  'grad_class': 2022,
  'crew_amount': 7,
  'advisors':
    ['appelbaum', 'burke', 'doyle', 'hoke', 'hale', 'pierce', 'regan'],
  'crew_spaces':
    {
      'appelbaum': 'the library',
      'burke': 'china',
      'doyle': 'make it happen',
      'hoke': 'sweden',
      'hale': 'dominican republic',
      'pierce': 'the great space',
      'regan': 'cuba',
    }
}

print(f"the {team_12['grade']} are the class of {team_12['grad_class']}")

print(f"there are {team_12['crew_amount']} crews in the class of 2022")

print("The advisors of Team 12 are: ")
for advisor in team_12['advisors'] :
  print(f"\t{advisor.title()}")

for advisors, spaces in team_12['crew_spaces'].items() :
  print(advisors.title() + " meets in " + spaces.title())

 