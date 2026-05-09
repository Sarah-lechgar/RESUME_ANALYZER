import matplotlib.pyplot as plt



def plot_skill_match(resume_skills, matched_skills):

    labels = ['Matched', 'Missing']

    values = [
        len(matched_skills),
        len(resume_skills) - len(matched_skills)
    ]


    fig, ax = plt.subplots()

    ax.pie(
        values,
        labels=labels,
        autopct='%1.1f%%'
    )

    ax.set_title('Skill Match Analysis')

    return fig