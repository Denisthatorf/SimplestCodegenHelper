#pragma once

namespace irl
{
    %%repeat
    class f_eventCallback_$$return_type$$input_types
	{
	typedef $$return_type (*functor_t)( $$input_args );

    public:
        f_eventCallback_$$return_type$$input_types (functor_t functor)
            : functionPtr  (functor) {}

        f_eventCallback_$$return_type$$input_types() = default;

        $$return_type operator() ( $$input_args ) const
        {
            return functionPtr( $$params );
        }

        functor_t functionPtr = nullptr;
    };
    %%end
} // namespace irl