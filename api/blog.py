from domain.model import *
from util.helper import *

# Initializing Http Status Code

status_code_created = 201
status_code_Not_Acceptable = 406
status_code_success = 200
status_coe_Not_found = 404


# Create post endpoint
@app.route('/blog/post/create', methods=['POST'])
def create_post():
    user_email = request.json['user_email']
    post_description = request.json['post_description']
    created_at = request.json['created_at']
    number_of_likes = request.json['number_of_likes']
    post_comments = request.json['post_comments']

    # instantiate helper class
    validation = Helper(user_email.lower(), created_at)

    if validation.validate_email() == 'failed':
        result = {'response': 'Invalid email address'}

        return result, status_code_Not_Acceptable
    else:
        new_post = Post(validation.validate_email(), post_description, validation.validate_created_at(),
                        number_of_likes, post_comments)
        db.session.add(new_post)
        db.session.commit()

    return post_schema.jsonify(new_post), status_code_created


# get All Posts
@app.route('/blog/post/all', methods=['GET'])
def get_all_posts():
    posts = Post.query.all()
    result = multi_post_schema.dump(posts)
    return jsonify(result), status_code_success


# get single Posts
@app.route('/blog/post/<post_id>', methods=['GET'])
def get_post_by_id(post_id):
    """"
       Return Single Post with specified post_id if not fund return 404 Http status code
    """
    post = Post.query.get_or_404(post_id)

    return post_schema.jsonify(post), status_code_success


# Update product
@app.route('/blog/post/update/<post_id>', methods=['PUT'])
def update_post(post_id):

    post = Post.query.get_or_404(post_id)

    user_email = request.json['user_email']
    post_description = request.json['post_description']
    created_at = request.json['created_at']
    number_of_likes = request.json['number_of_likes']
    post_comments = request.json['post_comments']

    # instantiate helper class
    validation = Helper(user_email.lower(), created_at)

    if validation.validate_email() == 'failed':
        result = {'response': 'Invalid email address'}

        return result, status_code_Not_Acceptable
    else:
        post.user_email = validation.validate_email()
        post.post_description = post_description
        post.created_at = validation.validate_created_at()
        post.number_of_likes = number_of_likes
        post.post_comments = post_comments

        db.session.commit()

    return post_schema.jsonify(post)


# delete Post
@app.route('/blog/post/delete/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    response_body = f"'post {post_id} deleted successfully'"
    message = {'response': response_body}
    db.session.delete(post)
    db.session.commit()

    return message, status_code_success
