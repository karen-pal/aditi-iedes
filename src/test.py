import main

main.db.create_all()

tag = main.Tag(tag_name='definición')
page = main.Page(title='heteronormatividad')

cards = [main.Card(card_type='text', page=page, content="""
Heteronorma o heteronormatividad es un régimen impuesto en la sociedad, en ámbito político y económico que impone las relaciones sexual-afectivas heterosexuales mediante diversos mecanismos médicos, artísticos, educativos, religiosos, jurídicos, etc. y mediante diversas instituciones que presentan la heterosexualidad.
"""
),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
         main.Card(card_type='text', page=page, content="LIPSUM"),
]

main.db.session.add(tag)
main.db.session.add(page)
[main.db.session.add(card) for card in cards]
main.db.session.commit()
