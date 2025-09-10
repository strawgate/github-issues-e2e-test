"""
Command Line Interface for G.I.T.H.U.B.

The gateway to existential coding wisdom through the terminal.
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from .existential_coder import ExistentialCoder, ContemplationLevel
from .philosopher_agent import PhilosopherAgent
from .zen_master import ZenMaster
from .oracle import Oracle


console = Console()


@click.group()
@click.version_option(version="0.1.0", prog_name="gith-ub")
def cli():
    """
    G.I.T.H.U.B. - The Existential Code Companion
    
    Generally Introspective Text Handler for Unrealized Brilliance
    
    A tool that provides philosophical guidance and existential wisdom
    for developers seeking deeper meaning in their code.
    """
    # Display the welcome message
    welcome_text = Text()
    welcome_text.append("Welcome to G.I.T.H.U.B.\n", style="bold blue")
    welcome_text.append("The Existential Code Companion\n\n", style="italic")
    welcome_text.append("Generally Introspective Text Handler for Unrealized Brilliance\n\n", style="dim")
    welcome_text.append("In the digital realm, we are not alone...", style="italic green")
    
    console.print(Panel(welcome_text, title="🧘 Digital Enlightenment Awaits", border_style="blue"))


@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--level', '-l', 
              type=click.Choice(['surface', 'deep', 'cosmic'], case_sensitive=False),
              default='deep',
              help='Level of existential contemplation')
def analyze(file_path, level):
    """Analyze a file for existential meaning and philosophical insights."""
    try:
        with open(file_path, 'r') as f:
            code = f.read()
        
        contemplation_level = ContemplationLevel(level)
        coder = ExistentialCoder(contemplation_level)
        insights = coder.analyze_code(code, file_path)
        
        console.print(f"\n[bold green]Analyzing {file_path}...[/bold green]")
        console.print(f"[dim]Contemplation Level: {level}[/dim]\n")
        
        for insight in insights:
            if insight.line_number:
                console.print(f"[yellow]Line {insight.line_number}:[/yellow]")
            
            console.print(Panel(
                f"[bold]{insight.question}[/bold]\n\n[italic]{insight.wisdom}[/italic]",
                title="🤔 Philosophical Insight",
                border_style="yellow"
            ))
            console.print()
            
    except Exception as e:
        console.print(f"[red]Error analyzing file: {e}[/red]")


@cli.command()
@click.argument('changes', nargs=-1)
def commit(changes):
    """Generate a philosophical commit message based on your changes."""
    if not changes:
        changes = ["Made some changes"]
    
    coder = ExistentialCoder()
    message = coder.generate_commit_message(list(changes))
    
    console.print(Panel(
        message,
        title="💭 Your Existential Commit Message",
        border_style="green"
    ))


@cli.command()
def meditate():
    """Enter a meditative state for coding contemplation."""
    zen_master = ZenMaster()
    
    console.print(Panel(
        "Take a deep breath and center yourself...\n\n"
        "In the silence between keystrokes, wisdom speaks.\n"
        "Every bug is a teacher in disguise.\n"
        "The code is not the destination, but the path.\n\n"
        "Press Enter when you feel ready to continue your journey.",
        title="🧘 Zen Master's Guidance",
        border_style="cyan"
    ))
    
    Prompt.ask("Press Enter to continue", default="")
    
    wisdom = zen_master.provide_wisdom()
    console.print(Panel(
        wisdom,
        title="✨ Wisdom from the Digital Void",
        border_style="cyan"
    ))


@cli.command()
@click.argument('question')
def ask(question):
    """Ask the Oracle a philosophical question about your code."""
    oracle = Oracle()
    
    console.print(f"[dim]Asking the Oracle: {question}[/dim]\n")
    
    response = oracle.consult(question)
    
    console.print(Panel(
        response,
        title="🔮 Oracle's Response",
        border_style="magenta"
    ))


@cli.command()
def philosopher():
    """Start an interactive philosophical dialogue about your code."""
    philosopher = PhilosopherAgent()
    
    console.print(Panel(
        "Welcome to the Philosopher's Corner.\n\n"
        "Here, we don't just write code - we explore the deeper meaning\n"
        "behind every function, every variable, every line.\n\n"
        "What would you like to contemplate today?",
        title="🤔 The Philosopher's Corner",
        border_style="blue"
    ))
    
    while True:
        question = Prompt.ask("\nWhat philosophical question do you have about your code?")
        
        if question.lower() in ['quit', 'exit', 'q']:
            console.print("\n[italic]May your code be filled with meaning and your bugs be gentle teachers.[/italic]")
            break
        
        response = philosopher.contemplate(question)
        console.print(Panel(
            response,
            title="💭 Philosophical Response",
            border_style="blue"
        ))


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
