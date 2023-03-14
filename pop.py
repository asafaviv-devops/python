### 15.10.22
### using pop methof
subscribers= ['tony@example.com','john@example.com','mary@example.com']
print(subscribers)
popend_subscriber = subscribers.pop()
print(subscribers)
print(popend_subscriber)
first_subscriber = subscribers.pop(0)
print("your first subscriber was " + first_subscriber)
subscribers= ['tony@example.com','john@example.com','mary@example.com']
print(subscribers)
subscribers.remove('john@example.com')
print(subscribers)
subscribe_by_mistake = 'tony@example.com'
subscribers.remove(subscribe_by_mistake)
print("\nThis person " + subscribe_by_mistake +' did not mean sign up')