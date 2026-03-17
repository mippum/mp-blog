def define_env(env):
    @env.macro
    def get_blog_posts(limit=5):
        nav = env.variables.get('navigation')
        if not nav:
            return []

        blog_posts = []

        for node in nav:
            if hasattr(node, 'posts'):
                print(" hasattr(node, 'posts')")
                blog_posts = node.posts
                break

        blog_posts.sort(key=lambda x: getattr(x.config, 'date', ''), reverse=True)
        
        return blog_posts[:limit]
