from my_app import db, app, Post, Comment, Tag

with app.app_context():
	db.drop_all()
	db.create_all()

	post1 = Post(title='Post The First', content='Content for the first post')
	post2 = Post(title='Post The Second', content='Content for the Second post')
	post3 = Post(title='Post The Third', content='Content for the third post')

	comment1 = Comment(content='Comment for the first post', post=post1)
	comment2 = Comment(content='Comment for the second post', post=post2)
	comment3 = Comment(content='Another comment for the second post', post_id=2)
	comment4 = Comment(content='Another comment for the first post', post_id=1)

	tag1 = Tag(name='animals')
	tag2 = Tag(name='tech')
	tag3 = Tag(name='cooking')
	tag4 = Tag(name='writing')

	post1.tags.append(tag1)  # Tag the first post with 'animals'
	post1.tags.append(tag4)  # Tag the first post with 'writing'
	post3.tags.append(tag3)  # Tag the third post with 'cooking'
	post3.tags.append(tag2)  # Tag the third post with 'tech'
	post3.tags.append(tag4)  # Tag the third post with 'writing'


	db.session.add_all([post1, post2, post3])
	db.session.add_all([comment1, comment2, comment3, comment4])
	db.session.add_all([tag1, tag2, tag3, tag4])

	db.session.commit()