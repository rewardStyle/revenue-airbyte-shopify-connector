ADVERTISERS_QUERY = "SELECT advertiser_homepage, affiliateId \
                    FROM `rewardstyle`.`Advertisers` \
                    WHERE SOURCE = 39 and active = 1 \
                    ORDER BY affiliateId ;"
SHOPIFY_ACCESS_TOKEN_PATH = "arn:aws:secretsmanager:us-east-1:{account_id}:secret:{{env}}/shopify/{{shop_id}}/shopify_access_token"