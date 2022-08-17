
class getErrorContext:
    errorsENG = {
        0: 'Debug',
        1: 'ClientHello is not supported!',
    }

    errorsRU = {
        0: 'Отладка',
        1: 'ClientHello не поддерживается!',
    }

#TODO: rewrite code below
    def whatIsThat(lang, context):
        try:
            if lang == 'RU':
                context = getErrorContext.errorsRU[context]
            elif lang == 'ENG':
                context = getErrorContext.errorsENG[context]
            elif lang != 'RU' and lang != 'ENG':
                context = getErrorContext.errorsENG[context]
        except KeyError:
            if lang == 'ENG':
                return "That's great question what happened."
            elif lang == 'RU':
                return "Хороший вопрос, что случилось."
            elif lang != 'RU' and lang != 'ENG':
                return "Хороший вопрос, что случилось."
        return context
