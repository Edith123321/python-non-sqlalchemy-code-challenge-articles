class Author:
    _authors = []  
    
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []  
        Author._authors.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter that maintains original name value"""
        pass  

    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def add_article(self, magazine, title):
        """Creates and returns a new article for this author"""
        article = Article(self, magazine, title)
        return article
    
    def topic_areas(self):
        categories = list(set(mag.category for mag in self.magazines()))
        return categories if categories else None


class Magazine:
    _magazines = []  # Store all magazine instances
    
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        else:
            self._name = name
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        else:
            self._category = category
        
        
        self._articles = []  # Store articles published in this magazine
        Magazine._magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name that validates length"""
        if not isinstance(value, str):
            return
        if 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        """Setter for category that validates type and length"""
        if not isinstance(value, str) or len(value) == 0:
            return
        self._category = value
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles))
    
    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None
    
    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        
        frequent_authors = [author for author, count in author_counts.items() if count > 2]
        return frequent_authors if frequent_authors else None
    
    @classmethod
    def top_publisher(cls):
        return max(cls._magazines, key=lambda mag: len(mag.articles()), default=None)


class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if not isinstance(title, str):
            self._title = str(title)
        else :
            self._title = title

        
        self._author = author
        self._magazine = magazine
        self._title = title
        
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        """Setter that maintains original title value"""
        pass  

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class.")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        self._magazine = value