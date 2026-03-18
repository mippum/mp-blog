def define_env(env):
    @env.macro
    def get_blog_posts(limit=5):
        nav = env.variables.get('navigation')
        if not nav:
            return []

        blog_posts = []
        for node in nav:
            if hasattr(node, 'posts'):
                blog_posts = node.posts
                break
        
        # [수정된 부분] x.config.date 자체가 아니라 그 안의 .created를 비교합니다.
        # getattr를 중첩해서 사용하여 date 객체가 없거나 created가 없어도 에러가 나지 않게 보호합니다.
        blog_posts.sort(
            key=lambda x: getattr(getattr(x.config, 'date', None), 'created', ""), 
            reverse=True
        )
        
        return blog_posts[:limit]