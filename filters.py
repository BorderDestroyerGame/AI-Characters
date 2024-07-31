from better_profanity import profanity

#region censoredWords
banned_words = {'fag', 'faggot', 'retard', 'retarded', ' nig ', 'nigger', 'nigga',
                'lesbo', 'negro', 'holocaust', 'nigg', 'jav', 'anglo', 'kkk', 'blacks',
                '9-11', '9/11', 'nine eleven', 'al qaeda', 'al qaida', 'autism', 'autistic',
                'loli', 'chink', 'El Chapo', 'fagfucker', 'faggots', 'faghag', 'faggit', 'fagged',
                'fags', 'homo', 'homophobe', 'homophobic', 'isis', 'j.a.p.', 'jigaboo', 'jiggaboo',
                'Jihad', 'klan', 'ku klux klan', 'lolicon', 'nazi', 'neonazi', 'neo-nazi', 'niggah',
                'niggerfaggot', 'niggers', 'niggaz', 'niggas', 'nigglet', 'niglet', 'osama bin laden',
                'paedo', 'paedophile', 'pedo', 'pedophile', 'pedophilia', 'pedobear', 'pedophiliac',
                'qanon', 'quasi', 'racist', 'rape', 'rapist', 'raper', 'raping', 'retards', 'sandy hook',
                'sexist', 'sexism', 'shota', 'shotacon', 'suicide', 'supremist', 'turk', 'school shooting',
                'white supremacists', 'white supremicy', 'xbox nigga', 'transphobic', 'molest', 'molester',
                "dyke", 'wigga', 'chink', 'fag', 'fagg', 'fagged', 'fagging', 'faggit', 'faggitt', 'faggot', 'faggs'
                'fagot', 'fagots', 'fags', 'faig', 'faigt', 'frigg', 'frigga', 'fuck-tard', 'fucktard', 'gringo',
                'h0m0', 'h0mo', 'hom0', 'jap', 'japs', 'lezbo', 'lezbos' , 'lezzie' , 'lezzies', 'lezzy', 'n1g', 'n1gg',
                'n1gga', 'n1gger', 'negro', 'nig', 'nigg', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger',
                'niggers', 'niggle', 'niglet'}
#endregion

whitelist = []

def checkOffensiveness(phrase):
    profanity.load_censor_words(custom_words=banned_words)
    flagged = False
    
    if profanity.contains_profanity(phrase):
        flagged = True
    
    return flagged