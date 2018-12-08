-- （1）	Find the content posted by the people who have more than 1000 followers
SELECT DISTINCT weibo_user.user_id, weibo_user.user_name, content
FROM weibo_user,
     user_post
WHERE weibo_user.follower_num > 1000
  AND weibo_user.user_id = user_post.poster_id;

-- （2）	Research the law and features of the content which post_number is more than 5.
SELECT DISTINCT weibo_user.user_id, weibo_user.user_name, content
FROM weibo_user,
     user_post
WHERE weibo_user.user_id = user_post.poster_id
  AND weibo_user.post_num > 5;

-- （3）	Please find the spammer and advertiser.
SELECT DISTINCT user_id, user_name
FROM weibo_user
WHERE weibo_user.is_spammer = 1;

select DISTINCT user_id, user_name
from user_post,
     weibo_user
where weibo_user.user_id = user_post.poster_id
  and
  (user_post.content like '%微信%'
    or user_post.content like '%V信%'
    or user_post.content like '%weixin%'
    or user_post.content like '%QQ%'
    or user_post.content like '%价格%'
    or user_post.content like '%联系%'
    or user_post.content like '%包邮%');

-- （4）	Finding zombie fans or followers in the table.
SELECT DISTINCT follower_id, follower
FROM follower_followee
WHERE guanzhu <= 5
  AND fensi <= 5
  AND post_num <= 5
  AND first_or_last = 'last';
