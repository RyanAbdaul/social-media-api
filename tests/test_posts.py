from app import schemas


def test_get_all_posts(authorized_client, _test_posts):
    res = authorized_client.get('/posts/')
    def validate(posts):
        return schemas.PostResponse(**posts)
    posts_map = map(validate, res.json())
    
    assert res.status_code == 200