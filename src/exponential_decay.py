# https://www.boot.dev/lessons/3ae4708e-0a55-4bae-8011-6de75bce05ab
def decayed_followers(intl_followers: int,
                      fraction_lost: float,
                      days: int) -> int:
    """remaining_total = quantity * ( retention_rate ^ time )"""
    remaining_followers = intl_followers * ((1 - fraction_lost) 

